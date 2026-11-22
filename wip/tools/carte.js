// Carte 3D : appels de dessin en vue rapprochée puis en vue d'ensemble (plantage iPhone de V310.6 si des milliers d'objets reviennent sous la vue d'ensemble)
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 1 }); await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 200)));
  await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 400; k++) { await p.waitForTimeout(1500); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.offsetParent && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } return G.mode + '|' + !!window.__zonesPretes; } catch (e) { return 'x'; } }); if (/^(play|guide)\|true/.test(st) && k > 3) break; }
  await p.waitForTimeout(4000);
  await p.evaluate(() => { const g = document.getElementById('guide'); if (g) g.remove(); const W = window.__W(); W.G.mode = 'play'; W.creatorSetHour(21); W.openMap3D(); });
  const cnt = () => p.evaluate(() => { const X = window.__X(), T = window.__T(), R = T.renderer; const ar = R.info.autoReset; R.info.autoReset = false; R.info.reset(); R.render(X.scene, X.camera); const r = [R.info.render.calls, Math.round(R.info.render.triangles / 1000), Math.round(X.camera.position.y), window.__W().M3.d]; R.info.autoReset = ar; return r; });
  for (const d of [300, 900, 2000, 4000, 9000]) { await p.evaluate(d => { const M3 = window.__W().M3; M3.d = d; if ('td' in M3) M3.td = d; if ('dT' in M3) M3.dT = d; }, d); await p.waitForTimeout(5000); console.log('CARTE d', d, JSON.stringify(await cnt())); await p.screenshot({ path: '/tmp/pc/carte_' + d + '.png', timeout: 240000 }); }
  console.log('ERR', errs.slice(0, 3).join(' | ') || 'none'); await b.close(); })().catch(e => { console.log('ERREUR', e.message.slice(0, 300)); process.exit(1); });
