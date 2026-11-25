const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')), out = process.argv[4]; fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 1280, height: 800 }, deviceScaleFactor: 1 });
  await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { window.__farDebug = 1; Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 300; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.getClientRects().length && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + !!window.__zonesPretes; } catch (e) { return 'x'; } }); if (/^play\|true/.test(st) && k > 3) break; }
  await p.evaluate(() => { const W = window.__W(), T = window.__T(), G = W.G; const g = document.getElementById('guide'); if (g) g.remove(); if (G.mode !== 'play') G.mode = 'play'; if (G.onFoot && G.parked) { G.inside = false; T.finishEnter({ own: true }); } window.__auto = () => ({ fwd: 0, side: 0, brake: true }); const PP = T.P; if (PP) PP.nightStart = false; W.creatorSetHour(14); });
  for (let k = 0; k < 200; k++) { const r = await p.evaluate(() => !!(window.__zonesPretes && window.__FARW && window.__FARW.ready)); if (r) break; await p.waitForTimeout(1000); }
  const R = await p.evaluate(async () => { const W = window.__W(), T = window.__T(), G = W.G, LM = W.LM; const wait = ms => new Promise(ok => setTimeout(ok, ms));
    if (G.onFoot && G.parked) { try { T.finishEnter({ own: true }); } catch (e) {} await wait(800); }
    window.__auto = () => ({ fwd: 0, side: 0, brake: false });
    const pts = Object.entries(LM).filter(([k, v]) => v && typeof v.x === 'number' && typeof v.z === 'number').map(([k, v]) => [k, v.x, v.z]);
    const want = (process => ['home', 'mont', 'parc', 'jungle', 'sud', 'mall', 'stade', 'archipel', 'aero', 'campagne', 'lac', 'port'])();
    const route = [['home', -196, 224], ['n1', 0, -1200], ['parc', -420, -2700], ['no', -1200, -1500], ['archipel', -1500, 400], ['sud', -300, 1000], ['f10e', 900, 800], ['est', 1600, -200], ['se', 1200, -1800], ['home2', -196, 224]];
    const r0 = W.renderer, rr = r0.render.bind(r0); r0.render = () => {}; // JS seul : le rendu logiciel du cloud ne dit rien de l'iPhone
    const gaps = []; let last = performance.now(), stop = false, cur = '';
    const raf = t => { const d = t - last; last = t; if (d > 34) gaps.push([Math.round(d), cur, Math.round(G.car.x), Math.round(G.car.z), (W.DEFER && W.DEFER.on) ? 'defer' : '']); if (!stop) requestAnimationFrame(raf); }; requestAnimationFrame(raf);
    const lt = []; try { new PerformanceObserver(l => l.getEntries().forEach(e => lt.push([Math.round(e.duration), cur]))).observe({ entryTypes: ['longtask'] }); } catch (e) {}
    const c = G.car; let frames = 0;
    for (let i = 0; i + 1 < route.length; i++) { const [ka, ax, az] = route[i], [kb, bx, bz] = route[i + 1]; cur = ka + '>' + kb; const L = Math.hypot(bx - ax, bz - az), h = Math.atan2(bx - ax, bz - az); const t0 = performance.now();
      while (true) { const s = (performance.now() - t0) / 1000 * 28; if (s > L) break; c.x = ax + (bx - ax) * s / L; c.z = az + (bz - az) * s / L; c.h = h; c.v = 28; c.jy = null; await wait(16); frames++; } }
    stop = true; r0.render = rr; window.__auto = null;
    return { lmkeys: pts.map(q => q[0] + ':' + Math.round(q[1]) + ',' + Math.round(q[2])).join(' '), route: route.map(r => r[0] + '(' + Math.round(r[1]) + ',' + Math.round(r[2]) + ')'), frames, gaps: gaps.sort((a, b) => b[0] - a[0]).slice(0, 40), longtasks: lt.sort((a, b) => b[0] - a[0]).slice(0, 25), nGaps: gaps.length }; });
  console.log(JSON.stringify(R)); await b.close(); })();
