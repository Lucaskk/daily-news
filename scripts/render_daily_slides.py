#!/usr/bin/env python3
"""Render one daily Markdown report as a self-contained, mobile-first reader."""

import argparse
from datetime import datetime, timezone
from html import escape
import json
from pathlib import Path
import re
from urllib.parse import urlsplit
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = Path(__file__).parent / "templates" / "daily-reader"
PUBLIC_BASE = "https://lucaskk.github.io/daily-news"
FIELDS = {
    "發佈時間": "published", "事件／發佈時間基準": "time_basis",
    "續報／去重": "history", "為何重要": "why", "重點摘要": "summary",
    "相關實體／概念": "entities", "不確定性／歧異": "uncertainty",
    "公司／產品": "product", "來源": "source_text",
}


def web_url(value):
    parts = urlsplit(value)
    if parts.scheme not in {"https", "http"} or not parts.netloc:
        raise ValueError(f"Expected a complete source URL: {value!r}")
    return value


def sources_in(text):
    sources = []
    for label, url in re.findall(r"\[([^\]]+)\]\((https?://[^\s]+)\)", text):
        item = {"label": label, "url": web_url(url)}
        if item not in sources:
            sources.append(item)
    return sources


def machine_time(text):
    match = re.match(r"(\d{4}-\d{2}-\d{2})(?: (\d{2}:\d{2}(?::\d{2})?))?", text)
    if not match:
        raise ValueError(f"Missing publication date: {text}")
    if not match[2]:
        return match[1]  # A date-only source must not gain an invented midnight.
    if "Asia/Taipei" not in text:
        raise ValueError(f"Timestamp must identify Asia/Taipei: {text}")
    value = datetime.fromisoformat(f"{match[1]}T{match[2]}")
    return value.replace(tzinfo=ZoneInfo("Asia/Taipei")).astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def parse_report(text):
    date_match = re.search(r"^date: (\d{4}-\d{2}-\d{2})$", text, re.M)
    if not date_match:
        raise ValueError("Report requires an ISO date in front matter")
    report = {"date": date_match[1], "stories": [], "followups": []}
    current = None
    collecting_facts = False
    followups = False
    for line in text.splitlines():
        line = line.strip()
        for label, key in [("研究截點", "cutoff"), ("全球新聞 24 小時視窗", "world_window"), ("科技／AI 產品 7 日視窗", "tech_window")]:
            if line.startswith(label + "｜"):
                report[key] = line.split("｜", 1)[1]
        heading = re.match(r"### (T?\d+)\. (.+)", line)
        if heading:
            current = {"id": heading[1].lower(), "rank": heading[1], "title": heading[2], "facts": []}
            current["category"] = "tech" if heading[1].startswith("T") else "world"
            report["stories"].append(current)
            collecting_facts = False
            continue
        if line.startswith("## "):
            current = None
            collecting_facts = False
            followups = line == "## 後續追蹤"
        if followups and line.startswith("- "):
            report["followups"].append(line[2:])
        if not current:
            continue
        if line == "關鍵事實：":
            collecting_facts = True
        elif "｜" in line and line.split("｜", 1)[0] in FIELDS:
            label, value = line.split("｜", 1)
            current[FIELDS[label]] = value
            collecting_facts = False
        elif collecting_facts and line.startswith("- "):
            current["facts"].append(line[2:])
    for story in report["stories"]:
        for key in ["published", "time_basis", "why", "history", "entities", "uncertainty", "source_text"]:
            if not story.get(key):
                raise ValueError(f"{story['rank']} missing {key}")
        story["sources"] = sources_in(story.pop("source_text"))
        story["datetime"] = machine_time(story["published"])
        if not story["sources"] or not story["facts"]:
            raise ValueError(f"{story['rank']} requires facts and sources")
    world = [s["rank"] for s in report["stories"] if s["category"] == "world"]
    if world != [str(n) for n in range(1, 11)]:
        raise ValueError("World stories must be exactly 1 through 10, in order")
    tech = [s for s in report["stories"] if s["category"] == "tech"]
    if [s["rank"] for s in tech] != [f"T{n}" for n in range(1, len(tech) + 1)]:
        raise ValueError("Product IDs must be consecutive")
    if report["stories"] != tech + [s for s in report["stories"] if s["category"] == "world"]:
        raise ValueError("Technology products must precede global stories")
    for key in ["cutoff", "world_window", "tech_window"]:
        if key not in report:
            raise ValueError(f"Report missing {key}")
    return report


def icon(name):
    svg = (TEMPLATE / "icons" / f"{name}.svg").read_text()
    svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
    return svg.replace("<svg", '<svg aria-hidden="true" focusable="false"', 1).strip()


def source_block(sources):
    links = "".join(
        f'<a href="{escape(s["url"], quote=True)}" target="_blank" rel="noopener noreferrer">'
        f'<strong>{escape(s["label"])}</strong><span>{escape(s["url"])}</span></a>'
        for s in sources
    )
    return f'<div class="sources"><h4>原始來源</h4>{links}</div>'


def media_html(media, folder, eager=False):
    if not media:
        return ""
    src = media["src"]
    if urlsplit(src).scheme:
        web_url(src)
    else:
        resolved = (folder / src).resolve()
        if not resolved.is_relative_to(folder.resolve()) or not resolved.is_file():
            raise ValueError(f"Missing local image: {src}")
    web_url(media["source_url"])
    fit = media.get("fit", "cover")
    if fit not in {"contain", "cover"}:
        raise ValueError("Image fit must be cover or contain")
    return (
        f'<!-- Image original: {escape(web_url(media.get("original_url", media["source_url"]))).replace("--", "&#45;&#45;")} -->'
        f'<figure class="story-media {fit}"><img src="{escape(src, quote=True)}" '
        f'alt="{escape(media["alt"], quote=True)}" width="1200" height="720" '
        f'loading="{"eager" if eager else "lazy"}" decoding="async">'
        f'<figcaption>{escape(media["caption"])} <a href="{escape(media["source_url"], quote=True)}" '
        f'target="_blank" rel="noopener noreferrer">{escape(media["credit"])}</a></figcaption></figure>'
    )


def story_html(story, media, folder, first=False):
    sid = story["id"]
    group = "科技產品" if story["category"] == "tech" else "全球焦點"
    tags = f'{group} <span>{escape(story["rank"])}</span>'
    source_labels = "".join(
        f'<a class="source-label" href="{escape(s["url"], quote=True)}" target="_blank" rel="noopener noreferrer">{escape(s["label"])}</a>'
        for s in story["sources"]
    )
    facts = "".join(f"<li>{escape(fact)}</li>" for fact in story["facts"])
    sections = [("事件背景與影響", story["why"]), ("事件與發佈依據", story["time_basis"]),
                ("收錄紀錄", story["history"]), ("尚待確認", story["uncertainty"]), ("相關實體與概念", story["entities"])]
    full = "".join(f'<h3>{label}</h3><p>{escape(value)}</p>' for label, value in sections)
    product = f'<p class="product">{escape(story["product"])}</p>' if story.get("product") else ""
    return f'''<article id="{sid}" class="story" data-category="{story['category']}" data-rank="{story['rank']}" aria-labelledby="title-{sid}">
      <p class="eyebrow">{tags}</p>
      {media_html(media, folder, first)}
      <h2 id="title-{sid}" tabindex="-1">{escape(story['title'])}</h2>
      <div class="metadata"><span>發佈時間</span><time datetime="{story['datetime']}">{escape(story['published'])}</time></div>
      <div class="byline"><span>出處</span>{source_labels}</div>
      {product}<p class="lead">{escape(story.get('summary', story['why']))}</p>
      <ul class="key-facts">{facts}</ul>
      <div class="article-actions">
        <button class="ask-action" type="button" data-ask="{sid}" aria-haspopup="dialog">{icon('message-circle')}<span>詢問後續問題</span></button>
        <details class="full-report" id="report-{sid}">
          <summary aria-controls="full-{sid}">{icon('file-text')}<span class="when-closed">完整報告</span><span class="when-open">收合報告</span>{icon('chevron-down')}</summary>
          <div class="report-body" id="full-{sid}">{full}{source_block(story['sources'])}</div>
        </details>
      </div>
    </article>'''


def script_json(value):
    return json.dumps(value, ensure_ascii=False).replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def render(report_path, media_path=None):
    report = parse_report(report_path.read_text())
    folder = report_path.parent
    date = report["date"]
    media_path = media_path or folder / f"presentation-{date}.json"
    media = json.loads(media_path.read_text()) if media_path.exists() else {"images": {}}
    stories = report["stories"]
    tech = [s for s in stories if s["category"] == "tech"]
    unknown = set(media.get("images", {})) - {s["id"] for s in stories}
    if unknown:
        raise ValueError(f"Images refer to unknown stories: {unknown}")
    dated_path = f"wiki/daily/{date[:4]}/{date[5:7]}/{date}/slides-{date}.html"
    report["url"] = f"{PUBLIC_BASE}/{dated_path}"
    for story in stories:
        story["url"] = f"{report['url']}#{story['id']}"
    articles = "".join(story_html(s, media.get("images", {}).get(s["id"]), folder, i == 0) for i, s in enumerate(stories))
    toc = "".join(f'<a href="#{s["id"]}" data-story-link="{s["id"]}"><span>{s["rank"]}</span>{escape(s["title"])}</a>' for s in stories)
    note_sources = [{"label": "每日報告", "url": report["url"].replace(f"slides-{date}.html", f"daily-news-{date}.md")},
                    {"label": "來源與時間筆記", "url": report["url"].replace(f"slides-{date}.html", f"source-notes-{date}.md")}]
    notes = "".join(f'<details class="note"><summary>{escape(title)}{icon("chevron-down")}</summary><div class="note-body"><p>{escape(value)}</p>{source_block(note_sources)}</div></details>'
                    for title, value in [("研究時間與範圍", f"研究截點：{report['cutoff']}。全球新聞：{report['world_window']}。科技產品：{report['tech_window']}。"),
                                         *[(f"後續追蹤 {i + 1}", f) for i, f in enumerate(report["followups"])]])
    # Everything needed for navigation and context handoff is bundled into this file.
    replacements = {
        "DATE": date, "CUTOFF": escape(report["cutoff"]), "TECH_COUNT": str(len(tech)),
        "FIRST_TECH": tech[0]["id"] if tech else "1", "TECH_DISABLED": "" if tech else 'aria-disabled="true"',
        "ARTICLES": articles, "TOC": toc, "NOTES": notes,
        "CSS": (TEMPLATE / "reader.css").read_text(), "JS": (TEMPLATE / "reader.js").read_text(),
        "DATA": script_json(report), "VERSION": datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d-%H%M%S-reader"),
        "ICON_LIST": icon("list"), "ICON_X": icon("x"), "ICON_COPY": icon("copy"),
        "ICON_PREV": icon("chevron-left"), "ICON_NEXT": icon("chevron-right"),
        "ICON_OPEN": icon("arrow-up-right"), "ICON_SUN": icon("sun"), "ICON_MOON": icon("moon"),
    }
    result = re.sub(r"@@([A-Z_]+)@@", lambda m: replacements[m[1]], (TEMPLATE / "reader.html").read_text())
    result = "\n".join(line.rstrip() for line in result.splitlines()) + "\n"
    output = folder / f"slides-{date}.html"
    output.write_text(result)
    return output, replacements["VERSION"]


def update_entries(output, version):
    relative = output.relative_to(ROOT / "wiki" / "daily").as_posix() + f"?v={version}"
    for path, target in [(ROOT / "wiki/daily/latest-slides.html", relative), (ROOT / "index.html", "wiki/daily/" + relative)]:
        path.write_text(f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0; url={escape(target, quote=True)}"><title>最新每日新聞</title></head><body><a href="{escape(target, quote=True)}">開啟最新每日新聞</a><script>location.replace({json.dumps(target)});</script></body></html>''')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--media", type=Path)
    parser.add_argument("--update-latest", action="store_true")
    args = parser.parse_args()
    output, version = render(args.report.resolve(), args.media)
    if args.update_latest:
        update_entries(output, version)
    print(f"Rendered {output}: {version}")


if __name__ == "__main__":
    main()
