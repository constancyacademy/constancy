// Portail itch sur ordinateur : en jeu sans toucher, puis « Garde ta partie » ouvre le QR code (lib qrcode autorisée) · node portail_qr.js page.html sortie_
const { chromium } = require('playwright'); const path = require('path');
(async () => { const page = path.resolve(process.argv[2]), out = process.argv[3] || '/tmp/pq_';
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 1100, height: 680 }, deviceScaleFactor: 1 }); await ctx.route(/^https?:/, r => /cdnjs\.cloudflare\.com\/ajax\/libs\/qrcode/.test(r.request().url()) ? r.continue() : r.abort());
  await ctx.addInitScript(() => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + page + '?nostat=1&portail=itch');
  await p.waitForFunction(() => (window.__stats || []).includes('partie-lancee'), null, { timeout: 900000 }); console.log('en jeu');
  await p.waitForTimeout(4000); await p.evaluate(() => document.getElementById('keepM') ? 0 : 0);
  await p.evaluate(() => { const e = document.createElement('button'); e.id = 'keepM'; document.body.appendChild(e); e.click(); });
  await p.waitForTimeout(25000); const r = await p.evaluate(() => ({ card: !!document.getElementById('pphone'), img: !!document.querySelector('#pqr img'), txt: (document.getElementById('pqr') || {}).textContent, stats: (window.__stats || []).filter(x => /portail-(garde|qr)/.test(x)) }));
  console.log(JSON.stringify(r)); await p.screenshot({ path: out + 'qr.png', timeout: 120000 }).catch(e => console.log('shot', e.message.slice(0, 80)));
  console.log('ERR', errs.length ? errs.slice(0, 3).join(' | ') : 'none'); await b.close(); })();
