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
  const R = await p.evaluate(async () => { const T = window.__T(), W = window.__W(), G = W.G, X = T.APTX; const E = X.list.find(e => e.a.id === 'villa'); if (!E) return { err: 'pas de villa', n: X.list.length };
    const d = E.door, out = { porte: [Math.round(d.x), Math.round(d.z)], eauPorte: W.isWater(d.x, d.z), eauDevant: W.isWater(d.x + Math.sin(d.h) * 3, d.z + Math.cos(d.h) * 3) };
    if (!G.onFoot) { try { T.toggleCar(); } catch (e) {} await new Promise(ok => setTimeout(ok, 900)); }
    const me = G.me; me.x = d.x + Math.sin(d.h) * 7; me.z = d.z + Math.cos(d.h) * 7; me.h = d.h + Math.PI; me.v = 0; me._lx = me.x; me._lz = me.z; G.snapCam = true; window.__auto = () => ({ fwd: 1, side: 0, brake: false });
    for (let i = 0; i < 80 && !G.inside; i++) { me.h = Math.atan2(d.x - me.x, d.z - me.z); await new Promise(ok => setTimeout(ok, 100)); }
    window.__auto = null; out.entre = G.inside || false; if (G.inside && T.leaveApt) { try { T.leaveApt(); } catch (e) {} await new Promise(ok => setTimeout(ok, 1500)); }
    G.inside = false; me.x = d.x; me.z = d.z; const tx = E.sp.x, tz = E.sp.z; me.h = Math.atan2(tx - me.x, tz - me.z); me._lx = me.x; me._lz = me.z; window.__auto = () => ({ fwd: 1, side: 0, brake: false }); let swim = 0, minH = 99, steps = 0;
    const dd0 = Math.hypot(tx - me.x, tz - me.z); for (let i = 0; i < 60; i++) { me.h = Math.atan2(tx - me.x, tz - me.z); await new Promise(ok => setTimeout(ok, 100)); if (G.swim || me.swim) swim++; minH = Math.min(minH, W.GH(me.x, me.z)); if (Math.hypot(tx - me.x, tz - me.z) < 10) break; }
    window.__auto = null; out.ponton = { depart: Math.round(dd0), arrivee: Math.round(Math.hypot(tx - me.x, tz - me.z)), nage: swim, solMin: +minH.toFixed(2) }; out.nage = !!(G.swim || me.swim); out.fin = [Math.round(me.x), Math.round(me.z)]; return out; });
  console.log(JSON.stringify(R)); await p.screenshot({ path: out + '/villa.png' }); await b.close(); })();
