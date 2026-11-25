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
  const shots = [['mi_jour', 14, [0, 40, -650], [0, 170, -1800]], ['haut_jour', 14, [250, 220, 500], [0, 170, -1800]], ['haut_nuit', 23, [250, 220, 500], [0, 170, -1800]], ['mi_nuit', 23, [0, 40, -650], [0, 170, -1800]]];
  for (const [nm, hr, p0, t0] of shots) {
    await p.evaluate(([hr, p0, t0]) => { const W = window.__W(); W.creatorSetHour(hr); window.__camK = () => ({ p: p0, t: t0, fov: 40 }); const sc = document.getElementById('screen'); if (sc) sc.style.visibility = 'hidden'; }, [hr, p0, t0]); await p.waitForTimeout(12000); await p.screenshot({ path: out + '/' + nm + '.png' }); }
  await b.close(); })();
