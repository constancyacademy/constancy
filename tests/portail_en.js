// Porte ng sans toucher : en jeu ? en anglais ? phrases non traduites · node portail_en.js page.html portail sortie_
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), por = process.argv[3] || 'ng', out = process.argv[4] || '/tmp/pe_';
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 }); await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(() => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message)); const t0 = Date.now(), T = () => ((Date.now() - t0) / 1000).toFixed(1) + 's';
  await p.goto('file://' + page + '?nostat=1&portail=' + por); await p.waitForTimeout(6000); await p.screenshot({ path: out + 'charge.png', timeout: 120000 }).catch(() => {}); console.log('charge', T());
  await p.waitForFunction(() => (window.__stats || []).includes('partie-lancee'), null, { timeout: 900000 }); console.log('EN JEU', T());
  await p.waitForTimeout(9000); await p.screenshot({ path: out + 'jeu.png', timeout: 120000 }).catch(() => {});
  const r = await p.evaluate(() => ({ lang: window.CST_LANG, overlay: !!document.getElementById('plLoad'), keys: !!document.getElementById('plKeys'), miss: (window.__i18nMiss ? window.__i18nMiss() : []).filter(x => /[a-zà-ÿ]{3}/i.test(x)).slice(0, 60), stats: (window.__stats || []).filter(x => /portail-en-jeu|portail-direct/.test(x)) }));
  console.log(JSON.stringify(r, null, 1)); console.log('ERR', errs.length ? errs.slice(0, 3).join(' | ') : 'none'); await b.close(); })();
