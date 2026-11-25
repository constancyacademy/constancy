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
  const res = [];
  for (const [label, pick] of [['avion de ligne (porte)', 'airbus'], ['bateau du Port-Est', 'bateau']]) {
    const r = await p.evaluate(async ([pick]) => { const W = window.__W(), T = window.__T(), G = W.G, P = T.P, wait = ms => new Promise(ok => setTimeout(ok, ms)); P.storyI = 9; if (!G.onFoot) { G.car.v = 0; G.car.alt = 0; T.toggleCar(); for (let i = 0; i < 20 && !G.onFoot; i++) await wait(250); }
      const L = T.rentals.filter(q => q.kind === pick && !(pick === 'airbus' && q.x === -60)); const q = L[0]; if (!q) return { err: 'aucun', n: L.length };
      G.me.x = q.x + (pick === 'airbus' ? 9 : 4); G.me.z = q.z; await wait(1200); T.toggleCar(); for (let i = 0; i < 40 && G.onFoot; i++) await wait(250); await wait(800); const ok = !G.onFoot && G.ride && G.ride.kind === pick; let moved = 0; if (ok) { const c = G.car, x0 = c.x, z0 = c.z; window.__auto = () => ({ fwd: 1, side: 0, brake: false }); await wait(5000); window.__auto = null; moved = Math.hypot(c.x - x0, c.z - z0); }
      return { blen: T.carMesh && T.carMesh.userData.blen, n: L.length, pris: ok, kind: G.ride && G.ride.kind, moved: +moved.toFixed(1), aide: ok ? '' : ((document.getElementById('help') || {}).textContent || '').slice(0, 100) }; }, [pick]);
    console.log(label, JSON.stringify(r)); await p.screenshot({ path: out + '/' + pick + '.png' }); }
  await b.close(); })();
