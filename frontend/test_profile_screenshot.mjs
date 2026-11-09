import puppeteer from 'puppeteer-core';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const screensDir = path.join(__dirname, 'public', 'screenshots');

async function run() {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu'],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 800, deviceScaleFactor: 1 });

  // Navigate to login page
  console.log('Navigating to login...');
  await page.goto('http://localhost:3000/login', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await new Promise((r) => setTimeout(r, 1000));

  // Fill login
  await page.type('input[type="email"]', 'customer@voltora.com');
  await page.type('input[type="password"]', 'customer123');
  
  // Submit
  const submitBtn = await page.$('button[type="submit"]');
  if (submitBtn) {
    await submitBtn.click();
    console.log('Submitted login form');
  }

  // Wait for redirect to /
  await new Promise((r) => setTimeout(r, 3000));

  const outPath = path.join(screensDir, 'profile-logged-in-1280px.png');
  await page.screenshot({ path: outPath, fullPage: false });
  console.log(`Saved logged-in screenshot: ${outPath}`);

  await browser.close();
}

run().catch((err) => {
  console.error('Error:', err);
  process.exit(1);
});
