#!/usr/bin/env python3
"""Process queued Taiwan-stock requests on this Mac and publish static pages."""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import fcntl
import json
import os
from pathlib import Path
import sys
import time
from typing import Any
import urllib.error
import urllib.parse
import urllib.request


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from generate_stock_analysis import StockAnalysisError, generate_analysis, now_taipei  # noqa: E402


DEFAULT_QUEUE_PATH = "wiki/stocks/requests"
DEFAULT_WATCHLIST = "2330"


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if key and key not in os.environ:
            os.environ[key] = value.strip().strip('"').strip("'")


def env(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


def github_headers() -> dict[str, str]:
    token = env("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "daily-news-stock-analysis",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def github_request(path: str, payload: dict[str, Any] | None = None, method: str | None = None) -> Any:
    repo = env("GITHUB_REPOSITORY", "Lucaskk/daily-news")
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers = github_headers()
    if data is not None:
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repo}{path}",
        data=data,
        headers=headers,
        method=method,
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8")
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API HTTP {exc.code}: {body[:500]}") from exc


def read_remote_requests(queue_path: str) -> list[dict[str, str]]:
    branch = env("GITHUB_BRANCH", "main")
    quoted = "/".join(urllib.parse.quote(part) for part in queue_path.strip("/").split("/"))
    try:
        entries = github_request(f"/contents/{quoted}?ref={urllib.parse.quote(branch)}")
    except RuntimeError as exc:
        if "HTTP 404" in str(exc):
            return []
        raise
    requests: list[dict[str, str]] = []
    for entry in entries if isinstance(entries, list) else []:
        if entry.get("type") != "file" or not str(entry.get("name", "")).endswith(".json"):
            continue
        payload = github_request(f"/contents/{entry['path']}?ref={urllib.parse.quote(branch)}")
        content = base64.b64decode(payload.get("content", "")).decode("utf-8")
        requests.append(json.loads(content))
    return requests


def read_local_requests(queue_path: Path) -> list[dict[str, str]]:
    requests = []
    if not queue_path.exists():
        return requests
    for path in sorted(queue_path.glob("*.json")):
        try:
            requests.append(json.loads(path.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError) as exc:
            print(f"Ignoring invalid request {path}: {exc}", file=sys.stderr)
    return requests


def collect_codes(requests: list[dict[str, str]], watchlist: str) -> list[str]:
    codes = []
    for value in watchlist.split(","):
        code = value.strip()
        if code.isdigit() and len(code) == 4:
            codes.append(code)
    for item in requests:
        code = str(item.get("code", "")).strip()
        if code.isdigit() and len(code) == 4:
            codes.append(code)
    return list(dict.fromkeys(codes))


def parse_request_time(value: str) -> dt.datetime | None:
    text = value.strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = f"{text[:-1]}+00:00"
    try:
        parsed = dt.datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def latest_requests_by_code(requests: list[dict[str, str]]) -> dict[str, dt.datetime]:
    latest: dict[str, dt.datetime] = {}
    for item in requests:
        code = str(item.get("code", "")).strip()
        requested_at = parse_request_time(str(item.get("requested_at", "")))
        if not (code.isdigit() and len(code) == 4 and requested_at):
            continue
        if code not in latest or requested_at > latest[code]:
            latest[code] = requested_at
    return latest


def generated_at(output_root: Path, code: str, date_value: dt.date) -> dt.datetime | None:
    target = output_root / f"{date_value:%Y/%m/%Y-%m-%d}" / code
    json_path = target / f"stock-analysis-{code}-{date_value.isoformat()}.json"
    if not json_path.exists():
        return None
    try:
        payload = json.loads(json_path.read_text(encoding="utf-8"))
        fetched_at = parse_request_time(str(payload.get("metadata", {}).get("fetched_at", "")))
    except (json.JSONDecodeError, OSError):
        return None
    return fetched_at


def needs_generation(
    output_root: Path,
    code: str,
    date_value: dt.date,
    requested_at: dt.datetime | None,
) -> bool:
    existing_at = generated_at(output_root, code, date_value)
    if existing_at is None:
        return True
    return requested_at is not None and requested_at > existing_at


def repo_relative(path: str | Path) -> str:
    path_obj = Path(path).resolve()
    return path_obj.relative_to(REPO_ROOT.resolve()).as_posix()


def publish_files(paths: list[Path], message: str) -> str:
    if not env("GITHUB_TOKEN"):
        raise RuntimeError("GITHUB_TOKEN is required to publish generated stock pages")
    branch = env("GITHUB_BRANCH", "main")
    ref = github_request(f"/git/ref/heads/{urllib.parse.quote(branch, safe='')}")
    parent_sha = ref["object"]["sha"]
    parent_commit = github_request(f"/git/commits/{parent_sha}")
    tree_elements = []
    for path in sorted(set(paths)):
        blob = github_request(
            "/git/blobs",
            {"content": base64.b64encode(path.read_bytes()).decode("ascii"), "encoding": "base64"},
            method="POST",
        )
        tree_elements.append({
            "path": repo_relative(path),
            "mode": "100644",
            "type": "blob",
            "sha": blob["sha"],
        })
    tree = github_request(
        "/git/trees",
        {"base_tree": parent_commit["tree"]["sha"], "tree": tree_elements},
        method="POST",
    )
    commit = github_request(
        "/git/commits",
        {"message": message, "tree": tree["sha"], "parents": [parent_sha]},
        method="POST",
    )
    github_request(
        f"/git/refs/heads/{urllib.parse.quote(branch, safe='')}",
        {"sha": commit["sha"], "force": False},
        method="PATCH",
    )
    return commit["sha"]


def write_status(output_root: Path, successful: list[str], failed: dict[str, str], skipped: list[str]) -> Path:
    status_path = output_root / "run-status.json"
    status_path.write_text(
        json.dumps({
            "run_at": now_taipei().replace(microsecond=0).isoformat(),
            "successful": successful,
            "failed": failed,
            "skipped_fresh_today": skipped,
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return status_path


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate queued stock analyses and publish them to GitHub Pages.")
    parser.add_argument("--force", action="store_true", help="Regenerate even if today's page already exists")
    parser.add_argument("--no-publish", action="store_true", help="Generate locally without publishing")
    parser.add_argument("--skip-remote", action="store_true", help="Only read local request files")
    parser.add_argument("--max-stocks", type=int, default=int(env("STOCK_ANALYSIS_MAX_PER_RUN", "12")))
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    load_dotenv(REPO_ROOT / ".env")
    args = parse_args(argv)
    output_root = REPO_ROOT / env("STOCK_ANALYSIS_OUTPUT_ROOT", "wiki/stocks")
    queue_path_text = env("STOCK_REQUEST_QUEUE_PATH", DEFAULT_QUEUE_PATH)
    queue_path = REPO_ROOT / queue_path_text
    lock_path = Path(env("STOCK_ANALYSIS_LOCK_FILE", "/tmp/daily-news-stock-analysis.lock"))
    lock_path.parent.mkdir(parents=True, exist_ok=True)

    with lock_path.open("w", encoding="utf-8") as lock_file:
        try:
            fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("Another stock-analysis run is already active")
            return 0

        requests = read_local_requests(queue_path)
        if not args.skip_remote:
            requests.extend(read_remote_requests(queue_path_text))
        codes = collect_codes(requests, env("STOCK_ANALYSIS_WATCHLIST", DEFAULT_WATCHLIST))[: max(args.max_stocks, 0)]
        latest_requests = latest_requests_by_code(requests)
        today = now_taipei().date()
        successful: list[str] = []
        skipped: list[str] = []
        failed: dict[str, str] = {}
        publish_paths: list[Path] = []

        for index, code in enumerate(codes):
            if not args.force and not needs_generation(output_root, code, today, latest_requests.get(code)):
                skipped.append(code)
                continue
            try:
                analysis = generate_analysis(
                    code,
                    output_root=output_root,
                    public_base_url=env("PUBLIC_STOCK_BASE_URL", "https://lucaskk.github.io/daily-news"),
                )
                artifacts = analysis["artifacts"]
                publish_paths.extend(Path(artifacts[key]) for key in (
                    "html_path", "json_path", "markdown_path", "latest_path", "code_latest_path", "index_path",
                ))
                successful.append(code)
            except (StockAnalysisError, RuntimeError, OSError) as exc:
                failed[code] = str(exc)[:500]
            if index + 1 < len(codes):
                time.sleep(float(env("STOCK_ANALYSIS_REQUEST_DELAY", "2")))

        status_path = write_status(output_root, successful, failed, skipped)
        if successful:
            publish_paths.append(status_path)
        if not args.no_publish and publish_paths:
            sha = publish_files(publish_paths, f"Publish stock analyses {today.isoformat()}")
            print(f"Published commit {sha}")
        print(json.dumps({"successful": successful, "failed": failed, "skipped": skipped}, ensure_ascii=False))
        return 1 if failed and not successful and not skipped else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
