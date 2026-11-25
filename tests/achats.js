const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')), out = process.argv[4]; fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 1 });
  await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { window.__farDebug = 1; Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 300; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.getClientRects().length && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + !!window.__zonesPretes; } catch (e) { return 'x'; } }); if (/^play\|true/.test(st) && k > 3) break; }
  await p.evaluate(() => { const W = window.__W(), T = window.__T(), G = W.G; const g = document.getElementById('guide'); if (g) g.remove(); if (G.mode !== 'play') G.mode = 'play'; if (G.onFoot && G.parked) { G.inside = false; T.finishEnter({ own: true }); } window.__auto = () => ({ fwd: 0, side: 0, brake: true }); const PP = T.P; if (PP) PP.nightStart = false; W.creatorSetHour(14); });
  for (let k = 0; k < 200; k++) { const r = await p.evaluate(() => !!(window.__zonesPretes)); if (r) break; await p.waitForTimeout(1000); }
  const R = await p.evaluate(async () => { const W = window.__W(), T = window.__T(), G = W.G, P = W.P, wait = ms => new Promise(ok => setTimeout(ok, ms)); const out = {};
    if (!G.onFoot) { G.wantExit = true; for (let i = 0; i < 20 && !G.onFoot; i++) await wait(300); }
    P.cash = 5000000; const L = W.LM; out.agences = [L.marine && [Math.round(L.marine.x), Math.round(L.marine.z)], L.airline && [Math.round(L.airline.x), Math.round(L.airline.z)]];
    ['trottneon', 'moto', 'jetski', 'yachtlux', 'avion'].forEach(id => T.vehBuy(id)); out.achetes = P.veh.slice(); out.cash = P.cash;
    out.trott = T.vehDeliver('trottneon'); const r1 = T.rentals.find(r => r.mine === 'trottneon'); out.trottD = r1 ? +Math.hypot(r1.x - G.me.x, r1.z - G.me.z).toFixed(1) : null;
    G.me.x = W.LM.marine.x; G.me.z = W.LM.marine.z; await wait(300); out.jet = T.vehDeliver('jetski'); out.yacht = T.vehDeliver('yachtlux'); const ry = T.rentals.find(r => r.mine === 'yachtlux'); out.yachtPos = ry ? [Math.round(ry.x), Math.round(ry.z), W.isWater(ry.x, ry.z)] : null;
    out.avion = T.vehDeliver('avion'); const ra = T.rentals.find(r => r.mine === 'avion'); out.avionPos = ra ? [Math.round(ra.x), Math.round(ra.z), G.gpsDest] : null;
    window.__yacht = ry ? [ry.x, ry.z] : null; return out; });
  console.log(JSON.stringify(R));
  // la trottinette néon : la prendre et rouler
  await p.evaluate(async () => { const W = window.__W(), T = window.__T(), G = W.G, wait = ms => new Promise(ok => setTimeout(ok, ms)); const r = T.rentals.find(r => r.mine === 'trottneon'); G.me.x = r.x + 1; G.me.z = r.z; await wait(200); });
  const R2 = await p.evaluate(async () => { const W = window.__W(), T = window.__T(), G = W.G, wait = ms => new Promise(ok => setTimeout(ok, ms)); const r = T.rentals.find(r => r.mine === 'trottneon'); G.me.x = r.x; G.me.z = r.z; W.toggleCar ? W.toggleCar() : null; for (let i = 0; i < 30 && G.onFoot; i++) await wait(200); const out = { monte: !G.onFoot, kind: G.ride.kind, mine: G.ride.mine }; window.__auto = () => ({ fwd: 1, side: 0, brake: false }); let vm = 0; const t0 = performance.now(); while (performance.now() - t0 < 12000) { await wait(200); vm = Math.max(vm, Math.abs(G.car.v)); } out.vmax = +vm.toFixed(1); window.__auto = () => ({ fwd: 0, side: 0, brake: true }); return out; });
  console.log(JSON.stringify(R2));
  await p.screenshot({ path: out + '/trott.png' });
  for (const [nm, k] of [['pav_marine', 'marine'], ['pav_airline', 'airline']]) { await p.evaluate(k => { const L = window.__W().LM[k]; window.__camK = () => ({ p: [L.x + 26, 22, L.z + 34], t: [L.x, 2, L.z + 6], fov: 50 }); }, k); await p.waitForTimeout(9000); await p.screenshot({ path: out + '/' + nm + '.png' }); }
  await p.evaluate(() => { const y = window.__yacht; if (y) window.__camK = () => ({ p: [y[0] + 40, 26, y[1] + 40], t: [y[0], 0, y[1]], fov: 50 }); }); await p.waitForTimeout(8000); await p.screenshot({ path: out + '/yacht.png' });
  await p.evaluate(() => { window.__camK = null; window.__T().openAgency('mer'); }); await p.waitForTimeout(2500); await p.screenshot({ path: out + '/agence_mer.png' });
  await b.close(); })();
