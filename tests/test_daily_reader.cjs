// Run with the existing Playwright installation; this test never opens ChatGPT.
const assert = require('node:assert/strict');
const { pathToFileURL } = require('node:url');
const path = require('node:path');
const fs = require('node:fs');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');

(async () => {
  const deck = process.argv[2];
  if (!deck) throw new Error('Pass the generated HTML path');
  const output = process.env.SCREENSHOT_DIR || '/tmp/daily-reader-qa';
  fs.mkdirSync(output, { recursive: true });
  const browser = await chromium.launch({ headless: true, ...(process.env.CHROME_EXECUTABLE ? { executablePath: process.env.CHROME_EXECUTABLE } : {}) });
  try {
    for (const viewport of [{ width: 320, height: 740 }, { width: 390, height: 844 }, { width: 768, height: 1024 }, { width: 1440, height: 1000 }]) {
      const context = await browser.newContext({ viewport, deviceScaleFactor: 1 });
      const page = await context.newPage();
      const errors = [];
      page.on('pageerror', error => errors.push(error.message));
      await page.route('https://chatgpt.com/**', () => { throw new Error('Tests must not submit article content'); });
      await page.goto(pathToFileURL(path.resolve(deck)).href, { waitUntil: 'load' });
      assert.equal(await page.locator('article').count(), 13);
      await page.locator('.story-media img').evaluateAll(images => images.forEach(img => { img.loading = 'eager'; }));
      await page.waitForFunction(() => Array.from(document.querySelectorAll('.story-media img')).every(img => img.complete && img.naturalWidth > 0));
      assert.equal(await page.locator('.story-media img').evaluateAll(images => images.every(img => img.complete && img.naturalWidth > 0)), true);
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true, 'horizontal overflow');
      assert.equal(await page.evaluate(() => document.querySelector('main').getBoundingClientRect().bottom <= document.querySelector('.reader-nav').getBoundingClientRect().top), true, 'navigation must not cover article text');
      assert.equal(await page.locator('.sections [aria-current="true"]').getAttribute('data-section'), 'tech');
      await page.screenshot({ path: path.join(output, `reader-${viewport.width}.png`) });

      const before = page.url();
      await page.locator('#report-t1 > summary').click();
      assert.equal(page.url(), before, 'Complete report must not navigate');
      assert.equal(await page.locator('#report-t1').getAttribute('open'), '');
      assert.equal(await page.locator('#full-t1 .sources a').count() > 0, true);
      await page.locator('#report-t1 > summary').scrollIntoViewIfNeeded();
      await page.screenshot({ path: path.join(output, `expanded-${viewport.width}.png`) });
      await page.locator('#report-t1 > summary').click();
      assert.equal(await page.locator('#report-t1').getAttribute('open'), null);

      await page.locator('[data-ask="t1"]').click();
      assert.equal(await page.locator('#ask-dialog').evaluate(dialog => dialog.open), true);
      await page.locator('#question').fill('上市地區 & 風險？');
      let url = new URL(await page.locator('#chatgpt-link').getAttribute('href'));
      let prompt = url.searchParams.get('prompt');
      assert.equal(url.origin, 'https://chatgpt.com');
      assert.ok(prompt.includes('Mate XT 2') && prompt.includes('上市地區 & 風險？'));
      assert.ok(prompt.includes('不確定性') && prompt.includes('Asia/Taipei') && prompt.includes('consumer.huawei.com'));
      assert.ok(!prompt.includes('WH-1000XM4C'), 'Do not include other articles');
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true);
      await page.screenshot({ path: path.join(output, `chatgpt-${viewport.width}.png`) });

      await page.locator('#question').fill('詳'.repeat(1900));
      assert.equal(await page.locator('#chatgpt-link').getAttribute('aria-disabled'), 'true');
      assert.equal(await page.locator('#chatgpt-link').getAttribute('href'), 'https://chatgpt.com/#native');
      await page.evaluate(() => Object.defineProperty(navigator, 'clipboard', { configurable: true, value: { writeText: async value => { window.testClipboard = value; } } }));
      await page.locator('#copy-context').click();
      assert.equal(await page.locator('#chatgpt-link').getAttribute('aria-disabled'), 'false');
      assert.ok((await page.evaluate(() => window.testClipboard)).includes('詳'.repeat(1900)));
      await page.locator('#question').fill('更'.repeat(1900));
      assert.equal(await page.locator('#chatgpt-link').getAttribute('aria-disabled'), 'true', 'Copy invalidates on question changes');
      await page.keyboard.press('Escape');
      assert.equal(await page.locator('[data-ask="t1"]').evaluate(el => el === document.activeElement), true);

      await page.locator('[data-section="world"]').click();
      assert.equal(new URL(page.url()).hash, '#1');
      await page.keyboard.press('ArrowRight');
      assert.equal(new URL(page.url()).hash, '#2');
      await page.locator('#open-index').click();
      await page.locator('#index-dialog [data-story-link="t3"]').click();
      assert.equal(new URL(page.url()).hash, '#t3');
      assert.equal(await page.locator('#title-t3').evaluate(el => el === document.activeElement), true, 'table of contents restores focus to article');
      await page.locator('[data-ask="t3"]').click();
      url = new URL(await page.locator('#chatgpt-link').getAttribute('href'));
      prompt = url.searchParams.get('prompt');
      assert.ok(prompt.includes('Wayve') && !prompt.includes('Mate XT 2'));
      assert.ok(prompt.includes('2026-09-03（Asia/Taipei；官方發布日期）'));
      await page.keyboard.press('Escape');

      // Exercise both failed clipboard methods; keep a manual selection fallback.
      await page.locator('[data-ask="t3"]').click();
      await page.evaluate(() => {
        Object.defineProperty(navigator, 'clipboard', { configurable: true, value: { writeText: async () => { throw new Error('denied'); } } });
        document.execCommand = () => false;
      });
      await page.locator('#copy-context').click();
      assert.ok((await page.locator('#copy-status').textContent()).includes('無法自動複製'));
      assert.equal(await page.locator('#context-text').evaluate(el => el.selectionEnd - el.selectionStart === el.value.length), true);
      await page.keyboard.press('Escape');
      await page.locator('#theme-toggle').click();
      assert.equal(await page.locator('html').getAttribute('data-theme'), 'light');
      await page.locator('[data-section="tech"]').click();
      await page.screenshot({ path: path.join(output, `light-${viewport.width}.png`) });
      assert.deepEqual(errors, []);
      await context.close();
    }
    console.log(`PASS: reader, expansion, navigation, ChatGPT payload, clipboard success/failure and theme scenarios across 320, 390, 768 and 1440px. Screenshots: ${output}`);
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
