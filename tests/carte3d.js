// Carte 3D : captures à 3 distances (noms nets, mer qui ne clignote pas, nuit gardée) · node carte3d.js page save [heure]
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')), HR = +(process.argv[4] || 20.5), MOB = !!process.env.MOB;
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext(MOB ? { viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true } : { viewport: { width: 900, height: 600 } });
  await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 200)));
  await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 200; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.getClientRects().length && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + !!window.__zonesPretes; } catch (e) { return 'x'; } }); if (/^(play|guide)\|true/.test(st) && k > 3) break; }
  await p.evaluate(hr => { const W = window.__W(), T = window.__T(), G = W.G; const g = document.getElementById('guide'); if (g) g.remove(); if (G.mode !== 'play') G.mode = 'play'; if (G.onFoot && G.parked) { G.inside = false; T.finishEnter({ own: true }); } W.creatorSetHour(hr); }, HR);
  await p.waitForTimeout(3000); await p.evaluate(() => window.__T().openMap3D());
  for (const d of [700, 1500, 4000]) { await p.evaluate(d => { const M3 = window.__T().M3; M3.dW = d; M3.d = d; }, d); await p.waitForTimeout(9000); await p.screenshot({ timeout: 300000, path: `/tmp/pc/carte_${MOB ? 'tel' : 'pc'}_${d}.png` }); console.log('vue', d); }
  console.log('ERR', errs.slice(0, 3).join(' | ') || 'none'); await b.close(); })().catch(e => { console.log('ERREUR', e.message.slice(0, 300)); process.exit(1); });
