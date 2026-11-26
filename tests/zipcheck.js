// Zip de plateforme lancé tel quel (index.html à la racine) : en jeu sans toucher ? anglais ? aucun texte ni requête vers constancy.fr ? · node zipcheck.js dossier_du_zip sortie_
const { chromium } = require('playwright'); const path = require('path');
(async () => { const dir = path.resolve(process.argv[2]), out = process.argv[3] || '/tmp/zc_';
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 }); const reqs = [];
  await ctx.route(/^https?:/, r => { reqs.push(r.request().url().slice(0, 90)); r.abort(); });
  await ctx.addInitScript(() => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message)); const t0 = Date.now(), T = () => ((Date.now() - t0) / 1000).toFixed(1) + 's';
  await p.goto('file://' + dir + '/index.html?nostat=1'); await p.waitForTimeout(7000); await p.screenshot({ path: out + 'charge.png', timeout: 120000 }).catch(() => {});
  await p.waitForFunction(() => (window.__stats || []).includes('partie-lancee'), null, { timeout: 900000 }); console.log('EN JEU', T());
  await p.waitForTimeout(12000); await p.screenshot({ path: out + 'jeu.png', timeout: 120000 }).catch(() => {});
  await p.evaluate(() => { try { document.getElementById('menuBtn').click(); } catch (e) {} }); await p.waitForTimeout(1500); await p.screenshot({ path: out + 'menu.png', timeout: 120000 }).catch(() => {});
  const r = await p.evaluate(() => ({ portail: window.CONSTANCY_PORTAIL, lang: window.CST_LANG, texteSite: /constancy\.fr/i.test(document.body.innerText), insta: /instagram|tiktok/i.test(document.body.innerHTML.replace(/<script[\s\S]*?<\/script>/g, '')), menu: (document.querySelector('.panel') || {}).innerText || '' }));
  r.menu = r.menu.replace(/\s+/g, ' ').slice(0, 300); console.log(JSON.stringify(r)); console.log('REQUETES', JSON.stringify([...new Set(reqs.map(u => u.split('/').slice(0, 3).join('/')))]));
  console.log('ERR', errs.length ? errs.slice(0, 3).join(' | ') : 'none'); await b.close(); })();
