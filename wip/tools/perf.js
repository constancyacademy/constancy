// R8 de l'expert : coût d'une image sur le trajet de la 1re mission et dans les 3 lieux de référence (centre-ville de nuit sous la pluie, plage de jour, périphérie sud en voiture rapide)
// Usage : node perf.js <page mkt> <save.json> [secondes par lieu]
// Sur la machine cloud (rendu logiciel) les images par seconde ne valent rien : on mesure ce qui ne dépend pas de l'appareil (appels de dessin, triangles) et le temps du code du jeu hors rendu (JS)
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')), SEC = +(process.argv[4] || 30);
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 1 });
  await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {}
    window.__pf = { on: false, fr: [] }; const raf = window.requestAnimationFrame.bind(window);
    window.requestAnimationFrame = cb => raf(t => { if (!window.__pf.on) return cb(t); window.__pf.r = 0; const a = performance.now(); cb(t); const d = performance.now() - a; window.__pf.fr.push([d, window.__pf.r]); }); }, save);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 200)));
  await p.goto('file://' + page + '?nostat=1&autostart=1&fps=1');
  for (let k = 0; k < 400; k++) { await p.waitForTimeout(1500); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.offsetParent && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + !!window.__zonesPretes; } catch (e) { return 'x'; } }); if (k % 10 === 0) console.log('attente', k, st); if (/^(play|guide)\|true/.test(st) && k > 3) break; }
  await p.waitForTimeout(5000);
  await p.evaluate(() => { const W = window.__W(), T = window.__T(), G = W.G; const g = document.getElementById('guide'); if (g) g.remove(); if (G.mode !== 'play') G.mode = 'play'; if (G.onFoot && G.parked) { G.inside = false; T.finishEnter({ own: true }); }
    const R = T.renderer, rr = R.render.bind(R); R.render = (s, c) => { const a = performance.now(); rr(s, c); window.__pf.r += performance.now() - a; window.__pf.calls = (window.__pf.calls || 0) + R.info.render.calls; window.__pf.tri = (window.__pf.tri || 0) + R.info.render.triangles; window.__pf.n = (window.__pf.n || 0) + 1; }; });
  const route = await p.evaluate(() => { const W = window.__W(), T = window.__T(), G = W.G, LM = W.LM; let pts = null; try { G.gpsDest = { x: LM.depot.x, z: LM.depot.z }; const gp = T.gpsRoute(); pts = gp && (gp.pts || gp.points || gp); } catch (e) {} if (!Array.isArray(pts) || pts.length < 2) pts = [{ x: LM.home.x, z: LM.home.z }, { x: LM.home.x, z: LM.depot.z }, { x: LM.depot.x, z: LM.depot.z }]; return pts.map(q => Array.isArray(q) ? { x: q[0], z: q[1] } : { x: q.x, z: q.z }); });
  console.log('TRAJET', route.length, 'points', JSON.stringify(route.slice(0, 6)));
  const south = await p.evaluate(() => { const W = window.__W(); for (let z = 700; z < 1400; z += 20) for (let x = -300; x < 300; x += 10) { try { if (W.roadH(x, z) != null && W.roadH(x, z + 30) != null) return { x, z, h: 0 }; } catch (e) {} } for (let z = 700; z < 1400; z += 20) for (let x = -300; x < 300; x += 10) { try { if (W.roadH(x, z) != null) return { x, z, h: 0 }; } catch (e) {} } return null; });
  const beach = await p.evaluate(() => { const B = window.__W().BEACH; const w = B && (B.walk[0] || B.swim[0]); return w ? { x: w.x !== undefined ? w.x : w[0], z: w.z !== undefined ? w.z : w[1] } : null; });
  console.log('SUD', JSON.stringify(south), 'PLAGE', JSON.stringify(beach));
  const run = async (name, args, step) => { await p.evaluate(put, args); await p.waitForTimeout(3000); await p.evaluate(() => { const f = window.__pf; f.fr = []; f.calls = f.tri = f.n = 0; f.on = true; });
    const t0 = Date.now(); let i = 0; while (Date.now() - t0 < SEC * 1000) { if (step) await p.evaluate(step, i++); await p.waitForTimeout(2000); }
    const r = await p.evaluate(() => { const f = window.__pf; f.on = false; const fr = f.fr.slice(5), js = fr.map(x => x[0] - x[1]).sort((a, b) => a - b), q = a => a.length ? a[Math.floor(a.length * 0.95)] : 0, av = a => a.length ? a.reduce((s, x) => s + x, 0) / a.length : 0; const W = window.__W(); return { images: fr.length, dessins: Math.round(f.calls / Math.max(1, f.n)), ktri: Math.round(f.tri / Math.max(1, f.n) / 1000), jsMoy: +av(js).toFixed(1), js95: +q(js).toFixed(1), rendu: +av(fr.map(x => x[1])).toFixed(0), kmh: Math.round(Math.abs(W.G.car.speed || 0) * 3.6), x: Math.round(W.G.car.x), z: Math.round(W.G.car.z), mem: performance.memory ? Math.round(performance.memory.usedJSHeapSize / 1048576) : 0 }; });
    console.log('LIEU', name, JSON.stringify(r)); await p.screenshot({ path: '/tmp/pc/perf_' + name + '.png', timeout: 240000 }); };
  const put = ([x, z, h, hr, wx, fwd]) => { const W = window.__W(), G = W.G; if (hr != null) W.creatorSetHour(hr); G.wxForce = wx; if (W.WX) W.WX.rain = wx || 0; if (x != null) { G.car.x = x; G.car.z = z; G.car.h = h; G.car.speed = 0; } window.__auto = () => ({ fwd: fwd, side: 0, brake: false }); };
  await p.evaluate(R => { window.__route = R; }, route);
  const only = (process.env.LIEUX || 'trajet,centre,plage,sud').split(',');
  if (only.includes('trajet')) await run('trajet-1re-mission', [route[0].x, route[0].z, 0, 9, 0, 0.6], i => { const R = window.__route, G = window.__W().G, n = R.length, u = Math.min(0.999, i / 14) * (n - 1), k = Math.floor(u), a = R[k], c = R[k + 1], t = u - k; G.car.x = a.x + (c.x - a.x) * t; G.car.z = a.z + (c.z - a.z) * t; G.car.h = Math.atan2(c.x - a.x, c.z - a.z); });
  if (only.includes('centre')) { const e = route[route.length - 1]; await run('centre-nuit-pluie', [e.x, e.z, Math.PI, 22.5, 0.85, 0.5], null); }
  if (only.includes('plage') && beach) await run('plage-jour', [beach.x, beach.z, 0, 13, 0, 0.4], null);
  if (only.includes('sud') && south) await run('sud-rapide', [south.x, south.z, 0, 15, 0, 1], null);
  console.log('ERR', errs.slice(0, 3).join(' | ') || 'none');
  await b.close(); })().catch(e => { console.log('ERREUR', e.message.slice(0, 300)); process.exit(1); });
