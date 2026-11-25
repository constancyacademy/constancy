const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')), out = process.argv[4]; fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 1 });
  await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { window.__farDebug = 1; Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 300; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.getClientRects().length && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + !!window.__zonesPretes; } catch (e) { return 'x'; } }); if (/^play\|true/.test(st) && k > 3) break; }
  await p.evaluate(() => { const W = window.__W(), T = window.__T(), G = W.G; const g = document.getElementById('guide'); if (g) g.remove(); if (G.mode !== 'play') G.mode = 'play'; if (G.onFoot && G.parked) { G.inside = false; T.finishEnter({ own: true }); } window.__auto = () => ({ fwd: 0, side: 0, brake: true }); const PP = T.P; if (PP) PP.nightStart = false; W.creatorSetHour(14); });
  for (let k = 0; k < 200; k++) { const r = await p.evaluate(() => !!(window.__zonesPretes && window.__FARW && window.__FARW.ready)); if (r) break; await p.waitForTimeout(1000); }
  const shotP = (async () => { for (let k = 0; k < 300; k++) { await p.waitForTimeout(300); if (await p.evaluate(() => window.__shotNow === 1).catch(() => false)) { await p.screenshot({ path: out + '/taxi.png' }); break; } } })();
  const R = await p.evaluate(async () => { const T = window.__T(), W = window.__W(), G = W.G, P = T.P; const out = { day: P.day };
    if (G.onFoot && G.parked) { try { T.finishEnter({ own: true }); } catch (e) {} await new Promise(ok => setTimeout(ok, 800)); }
    G.mission = null; P.tx = null; P.day = Math.max(2, P.day || 1); T.txStart(); out.lance = T.TX.on; out.barre = !!document.getElementById('txBar'); out.modele = T.TX.a && T.TX.a.model;
    if (!T.TX.on) return out; window.__shotNow = 1; await new Promise(ok => setTimeout(ok, 1500));
    const c = G.car, t0 = performance.now(); while (T.TX.on && performance.now() - t0 < 120000) { const a = T.TX.a; if (a) { c.x = a.x - Math.sin(a.h) * 7; c.z = a.z - Math.cos(a.h) * 7; c.h = a.h; c.v = a.speed || 0; c.jy = null; } await new Promise(ok => setTimeout(ok, 150)); }
    out.fini = !T.TX.on; out.aide = (document.getElementById('help') || {}).textContent; out.stats = (window.__stats || []).filter(x => /taxi/.test(x)); return out; });
  console.log(JSON.stringify(R, null, 1)); await b.close(); })();
