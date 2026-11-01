// Combine the sketch sheets into one A3-landscape PDF and render PNG previews.
// Run after make_sketches.py:  node design/sketches/make_pdf.js
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const dir = __dirname;
const sheets = ['1-laptop-bag', '2-big-pack', '3-weight-system'];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1680, height: 1188 } });

  for (const name of sheets) {
    const svg = fs.readFileSync(path.join(dir, `${name}.svg`), 'utf8');
    await page.setContent(`<html><body style="margin:0">${svg}</body></html>`);
    await page.screenshot({ path: path.join(dir, `${name}.png`) });
  }

  const pages = sheets
    .map((n) => fs.readFileSync(path.join(dir, `${n}.svg`), 'utf8')
      .replace('<svg ', '<svg style="width:420mm;height:297mm;display:block" '))
    .join('<div style="break-after:page"></div>');
  await page.setContent(`<html><head><style>@page{size:A3 landscape;margin:0}body{margin:0}</style></head><body>${pages}</body></html>`);
  await page.pdf({ path: path.join(dir, 'heavy-bag-concept-sketches.pdf'), format: 'A3', landscape: true, printBackground: true });

  await browser.close();
  console.log('wrote PNGs and heavy-bag-concept-sketches.pdf');
})();
