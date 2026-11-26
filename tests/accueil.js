// Écran d'accueil d'un joueur qui revient, en téléphone (iPhone 14 émulé) : une capture par plan · node accueil.js page.html save.json sortie_ [secondes]
// (Thomas 26/11 9h51 : « gros bug d'affichage, les immeubles sont noirs » à l'accueil)
const { chromium, devices } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')), out = process.argv[4] || '/tmp/acc_', dur = Number(process.argv[5] || 46);
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ ...devices['iPhone 14'], deviceScaleFactor: 1 });
  await ctx.route(/^https?:\/\/(?!cdnjs|cdn\.jsdelivr|fonts\.)/, r => r.abort());
  await ctx.addInitScript(s => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); { const mm = window.matchMedia.bind(window), fk = (q, v) => ({ matches: v, media: q, onchange: null, addListener() {}, removeListener() {}, addEventListener() {}, removeEventListener() {} }); window.matchMedia = q => /pointer\s*:\s*fine/.test(q) ? fk(q, false) : /pointer\s*:\s*coarse/.test(q) ? fk(q, true) : mm(q); } try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message)); await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 300; k++) { await p.waitForTimeout(1000); const ok = await p.evaluate(() => !!document.getElementById('cont')).catch(() => false); if (ok) break; }
  await p.evaluate(() => { const g = document.getElementById('guide'); if (g) g.remove(); });
  const t0 = Date.now(); let i = 0;
  while ((Date.now() - t0) / 1000 < dur) { await p.waitForTimeout(3500); await p.screenshot({ path: out + String(i).padStart(2, '0') + '.png', timeout: 60000 }).catch(() => {}); i++; }
  console.log('CAPTURES', i, 'ERR', errs.length ? errs.slice(0, 3).join(' | ') : 'none'); await b.close(); })();
