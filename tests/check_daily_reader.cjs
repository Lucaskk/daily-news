// Reusable smoke test for any dated reader; never sends article data to ChatGPT.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const { pathToFileURL } = require('node:url');
const path = require('node:path');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');

(async () => {
  const target = process.argv[2];
  if (!target) throw new Error('Pass a deck URL or local HTML path');
  const url = /^https?:/.test(target) ? target : pathToFileURL(path.resolve(target)).href;
  const out = process.env.SCREENSHOT_DIR || '/tmp/daily-news-smoke';
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({ headless: true, ...(process.env.CHROME_EXECUTABLE ? { executablePath: process.env.CHROME_EXECUTABLE } : {}) });
  try {
    for (const width of [320, 390, 1440]) {
      const page = await browser.newPage({ viewport: { width, height: 900 } });
      const errors = [];
      page.on('pageerror', error => errors.push(error.message));
      await page.route('https://chatgpt.com/**', route => route.abort());
      await page.goto(url, { waitUntil: 'load' });
      const report = JSON.parse(await page.locator('#report-data').textContent());
      assert.equal(await page.locator('article').count(), report.stories.length);
      assert.deepEqual(report.stories.filter(s => s.category === 'world').map(s => s.rank), Array.from({ length: 10 }, (_, i) => String(i + 1)));
      const first = report.stories[0];
      const other = report.stories[1];
      await page.locator('.story-media img').evaluateAll(images => images.forEach(i => { i.loading = 'eager'; }));
      await page.waitForFunction(() => [...document.images].every(i => i.complete && i.naturalWidth > 0));
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
      const before = page.url();
      await page.locator(`#report-${first.id} > summary`).click();
      assert.equal(page.url(), before);
      assert.equal(await page.locator(`#report-${first.id}`).getAttribute('open'), '');
      assert.ok(await page.locator(`#full-${first.id} .sources a`).count());
      await page.locator(`#report-${first.id} > summary`).click();
      await page.locator(`[data-ask="${first.id}"]`).click();
      await page.locator('#question').fill('請說明後續風險');
      const payload = await page.locator('#context-text').inputValue();
      assert.ok(payload.includes(first.title));
      assert.ok(payload.includes(first.sources[0].url));
      assert.ok(payload.includes('請說明後續風險'));
      assert.ok(!payload.includes(other.title));
      await page.keyboard.press('Escape');
      await page.locator('[data-section="world"]').click();
      await page.keyboard.press('ArrowRight');
      assert.equal(new URL(page.url()).hash, '#2');
      await page.locator(`#title-${first.id}`).evaluate(el => el.scrollIntoView());
      await page.screenshot({ path: path.join(out, `reader-${width}.png`) });
      assert.deepEqual(errors, []);
      await page.close();
    }
    console.log(`PASS: 320/390/1440px, images, inline report, per-article context, keyboard navigation. ${out}`);
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
