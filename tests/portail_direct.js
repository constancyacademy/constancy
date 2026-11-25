// Portail : le joueur arrive dans l'iframe et ne touche RIEN · on mesure quand il est en jeu · node portail_direct.js page.html portail sortie_
const { chromium } = require('playwright'); const path = require('path');
(async () => { const page = path.resolve(process.argv[2]), por = process.argv[3] || 'itch', out = process.argv[4] || '/tmp/pd_';
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio', '--autoplay-policy=user-gesture-required'] });
  const ctx = await b.newContext({ viewport: { width: 960, height: 540 }, deviceScaleFactor: 1 }); await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(() => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message)); const t0 = Date.now(); const T = () => ((Date.now() - t0) / 1000).toFixed(1) + 's';
  await p.goto('file://' + page + '?nostat=1&portail=' + por);
  let shot = 0, last = '';
  for (let k = 0; k < 400; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { try { const W = window.__W(); return W.G.mode + '|dream=' + !!(W.DREAM && W.DREAM.on) + '|mir=' + !!(W.MIR && W.MIR.on) + '|stats=' + (window.__stats || []).filter(x => /jouer|portail|perso-cree|partie-lancee|reve-debut|ecran-email/.test(x)).join(','); } catch (e) { return 'x'; } });
    if (st !== last) { console.log(T(), st); last = st; }
    if (/partie-lancee/.test(st)) { await p.waitForTimeout(6000); await p.screenshot({ path: out + 'jeu.png' }); console.log('EN JEU', T()); break; } }
  console.log('ERR', errs.length ? errs.slice(0, 3).join(' | ') : 'none'); await b.close(); })();
