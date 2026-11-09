import puppeteer from 'puppeteer-core';
import path from 'path';
import { fileURLToPath } from 'url';
import fs from 'fs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const screensDir = path.join(__dirname, 'public', 'screenshots');

if (!fs.existsSync(screensDir)) {
  fs.mkdirSync(screensDir, { recursive: true });
}

const viewports = [
  { name: 'screenshot-1440px.png', width: 1440, height: 900 },
  { name: 'screenshot-1024px.png', width: 1024, height: 768 },
  { name: 'screenshot-768px.png', width: 768, height: 1024 },
  { name: 'screenshot-375px.png', width: 375, height: 812 },
];

async function run() {
  console.log('Launching Chrome via puppeteer-core...');
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu'],
  });

  const page = await browser.newPage();

  page.on('console', (msg) => console.log(`[PAGE LOG] ${msg.type()}: ${msg.text()}`));
  page.on('pageerror', (err) => console.log(`[PAGE ERROR]`, err));

  console.log('Warming up server...');
  await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await new Promise((r) => setTimeout(r, 1500));

  for (const vp of viewports) {
    console.log(`Capturing ${vp.width}x${vp.height} -> ${vp.name}...`);
    await page.setViewport({ width: vp.width, height: vp.height, deviceScaleFactor: 1 });
    await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded', timeout: 30000 });
    // Wait for animations and layout
    await new Promise((r) => setTimeout(r, 2000));
    
    const outPath = path.join(screensDir, vp.name);
    await page.screenshot({ path: outPath, fullPage: false });
    console.log(`Saved: ${outPath} (${fs.statSync(outPath).size} bytes)`);

    // Also capture full-page screenshot
    const fullPath = path.join(screensDir, vp.name.replace('.png', '-full.png'));
    await page.screenshot({ path: fullPath, fullPage: true });
    console.log(`Saved full: ${fullPath} (${fs.statSync(fullPath).size} bytes)`);
  }

  await browser.close();
  console.log('All screenshots captured successfully!');
}

run().catch((err) => {
  console.error('Error capturing screenshots:', err);
  process.exit(1);
});
