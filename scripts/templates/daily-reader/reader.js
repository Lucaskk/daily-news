(() => {
  'use strict';
  const report = JSON.parse(document.getElementById('report-data').textContent);
  const stories = report.stories;
  const byId = new Map(stories.map(story => [story.id, story]));
  const articles = Array.from(document.querySelectorAll('article.story'));
  const sections = [...articles, document.getElementById('notes')];
  const askDialog = document.getElementById('ask-dialog');
  const indexDialog = document.getElementById('index-dialog');
  const question = document.getElementById('question');
  const contextText = document.getElementById('context-text');
  const chatLink = document.getElementById('chatgpt-link');
  const note = document.getElementById('handoff-note');
  const status = document.getElementById('copy-status');
  const themeButton = document.getElementById('theme-toggle');
  const prev = document.getElementById('prev');
  const next = document.getElementById('next');
  let current = 0;
  let selected = null;
  let opener = null;
  let copiedContext = '';
  let currentContext = '';
  const MAX_LINK_LENGTH = 12000;

  function setTheme(theme) {
    document.documentElement.dataset.theme = theme;
    const label = theme === 'dark' ? '切換淺色' : '切換深色';
    themeButton.title = label;
    themeButton.setAttribute('aria-label', label);
  }
  try { setTheme(localStorage.getItem('daily-reader-theme') === 'light' ? 'light' : 'dark'); } catch (_) { setTheme('dark'); }
  themeButton.addEventListener('click', () => {
    const theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    setTheme(theme);
    try { localStorage.setItem('daily-reader-theme', theme); } catch (_) { /* Private storage can be unavailable. */ }
  });

  function updatePosition() {
    const threshold = document.querySelector('.masthead').getBoundingClientRect().height + 36;
    let position = 0;
    sections.forEach((section, i) => { if (section.getBoundingClientRect().top <= threshold) position = i; });
    current = position;
    const story = stories[current];
    const label = story
      ? `${story.category === 'tech' ? '科技' : '全球'} ${story.rank.replace('T', '')} / ${stories.filter(s => s.category === story.category).length}`
      : '研究備註';
    const counter = document.getElementById('position');
    if (counter.textContent !== label) counter.textContent = label;
    prev.disabled = current === 0;
    next.disabled = current === sections.length - 1;
    document.querySelectorAll('[data-section]').forEach(link => {
      link.setAttribute('aria-current', String(link.dataset.section === (story ? story.category : 'notes')));
    });
  }

  function jump(id, push = true) {
    const target = sections.find(section => section.id === id);
    if (!target) return;
    if (push && location.hash !== `#${id}`) history.pushState(null, '', `#${id}`);
    target.scrollIntoView({ behavior: 'instant', block: 'start' });
    const title = target.querySelector('h2');
    if (title) { title.tabIndex = -1; title.focus({ preventScroll: true }); }
    updatePosition();
  }
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    if (link.classList.contains('skip-link')) return;
    link.addEventListener('click', event => {
      const id = link.hash.slice(1);
      if (!sections.some(section => section.id === id)) return;
      event.preventDefault();
      if (indexDialog.open) { opener = null; indexDialog.close(); }
      jump(id);
    });
  });
  prev.addEventListener('click', () => jump(sections[Math.max(0, current - 1)].id));
  next.addEventListener('click', () => jump(sections[Math.min(sections.length - 1, current + 1)].id));
  let scrollPending = false;
  document.getElementById('content').addEventListener('scroll', () => {
    if (!scrollPending) requestAnimationFrame(() => { updatePosition(); scrollPending = false; });
    scrollPending = true;
  }, { passive: true });
  window.addEventListener('resize', updatePosition);
  window.addEventListener('hashchange', () => jump(location.hash.slice(1), false));
  window.addEventListener('keydown', event => {
    if (askDialog.open || indexDialog.open || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey ||
        event.target.closest('input, textarea, select, button, summary, [contenteditable]')) return;
    if (event.key === 'ArrowLeft') { event.preventDefault(); prev.click(); }
    if (event.key === 'ArrowRight') { event.preventDefault(); next.click(); }
  });

  function openDialog(dialog, source) {
    opener = source;
    dialog.showModal();
    document.body.classList.add('modal-open');
  }
  for (const dialog of [askDialog, indexDialog]) {
    dialog.querySelector('[data-close]').addEventListener('click', () => dialog.close());
    dialog.addEventListener('close', () => {
      document.body.classList.remove('modal-open');
      if (opener && !indexDialog.open && !askDialog.open) opener.focus({ preventScroll: true });
    });
    dialog.addEventListener('click', event => {
      if (event.target !== dialog) return;
      const rect = dialog.getBoundingClientRect();
      if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
    });
  }
  document.getElementById('open-index').addEventListener('click', event => openDialog(indexDialog, event.currentTarget));

  function makeContext(story, userQuestion) {
    const lines = [
      '請使用繁體中文，根據下列新聞筆記協助我討論後續問題。區分已知事實、來源主張與推測；若需要最新資訊，請重新查證並附來源。',
      '', `新聞標題：${story.title}`, `發佈時間：${story.published}`, `研究截點：${report.cutoff}`,
      `本文連結：${story.url}`, '', `摘要：${story.summary || story.why}`, '', '關鍵事實：',
      ...story.facts.map(fact => `- ${fact}`), '', `背景與影響：${story.why}`,
      `事件與發佈依據：${story.time_basis}`, `不確定性：${story.uncertainty}`, `相關實體與概念：${story.entities}`,
    ];
    if (story.product) lines.push(`公司與產品：${story.product}`);
    if (story.title.startsWith('續報｜')) lines.push(`前次收錄與新進展：${story.history}`);
    lines.push('', '原始來源：', ...story.sources.map(source => `${source.label}\n${source.url}`), '',
      `我的問題：${userQuestion.trim() || '這篇新聞還有哪些值得追問的重點？請列出後續問題，並指出回答它們需要哪些資料。'}`);
    return lines.join('\n');
  }

  function updateHandoff() {
    if (!selected) return;
    currentContext = makeContext(selected, question.value);
    contextText.value = currentContext;
    const url = new URL('https://chatgpt.com/');
    url.searchParams.set('prompt', currentContext);
    const oversized = url.href.length > MAX_LINK_LENGTH;
    chatLink.href = oversized ? 'https://chatgpt.com/#native' : url.href;
    const ready = !oversized || copiedContext === currentContext;
    chatLink.setAttribute('aria-disabled', String(!ready));
    note.textContent = oversized
      ? (ready ? '完整內容已複製。開啟 ChatGPT 後可貼上提問。' : '文章與問題較長，請先複製完整內容，再開啟 ChatGPT 貼上。')
      : 'Safari 將依裝置設定開啟 ChatGPT App 或網頁。若未帶入文字，可使用右側複製按鈕。';
  }
  document.querySelectorAll('[data-ask]').forEach(button => {
    button.addEventListener('click', () => {
      selected = byId.get(button.dataset.ask);
      document.getElementById('ask-story-title').textContent = selected.title;
      question.value = '';
      status.textContent = '';
      copiedContext = '';
      askDialog.querySelector('.context-details').open = false;
      updateHandoff();
      openDialog(askDialog, button);
    });
  });
  question.addEventListener('input', () => { status.textContent = ''; updateHandoff(); });
  chatLink.addEventListener('click', event => {
    if (chatLink.getAttribute('aria-disabled') === 'true') {
      event.preventDefault();
      status.textContent = '請先複製完整內容。';
      document.getElementById('copy-context').focus();
    }
    // Keep a normal, user-initiated HTTPS navigation so Safari can hand off to iOS.
  });
  document.getElementById('copy-context').addEventListener('click', async () => {
    const pending = currentContext;
    let copied = false;
    try { await navigator.clipboard.writeText(pending); copied = true; } catch (_) {
      askDialog.querySelector('.context-details').open = true;
      contextText.focus();
      contextText.select();
      contextText.setSelectionRange(0, contextText.value.length);
      try { copied = document.execCommand('copy'); } catch (_) { /* Keep the text selected for manual copying. */ }
    }
    if (copied) {
      copiedContext = pending;
      status.textContent = '已複製完整文章與問題。';
      updateHandoff();
    } else {
      status.textContent = '無法自動複製。完整文字已選取，可長按複製。';
    }
  });
  contextText.addEventListener('copy', () => {
    if (contextText.selectionStart === 0 && contextText.selectionEnd === contextText.value.length) {
      copiedContext = contextText.value;
      setTimeout(updateHandoff, 0);
    }
  });
  document.querySelectorAll('.story-media img').forEach(img => {
    const failure = () => {
      const figure = img.closest('figure');
      figure.classList.add('image-failed');
      figure.querySelector('figcaption').prepend('圖片暫時無法載入。');
    };
    img.addEventListener('error', failure, { once: true });
    if (img.complete && !img.naturalWidth) failure();
  });
  window.addEventListener('load', () => {
    if (location.hash) jump(location.hash.slice(1), false);
    updatePosition();
  });
  updatePosition();
})();
