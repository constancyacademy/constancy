// Usage : node tests/voitures_prises.js <page-test.html> <save.json>
// Thomas 24/11 10h34 : les voitures autour de la map doivent pouvoir être prises, sauf les voitures de luxe de l'Archipel (débloquées après plusieurs missions)
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); window.__norender = 1; try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 200)));
  await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 300; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.getClientRects().length && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + !!window.__zonesPretes; } catch (e) { return 'x'; } }); if (/^play\|true/.test(st) && k > 3) break; }
  await p.evaluate(() => { const W = window.__W(), T = window.__T(), G = W.G; const g = document.getElementById('guide'); if (g) g.remove(); if (G.mode !== 'play') G.mode = 'play'; if (G.onFoot && G.parked) { G.inside = false; T.finishEnter({ own: true }); } window.__auto = () => ({ fwd: 0, side: 0, brake: true }); });
  for (let k = 0; k < 150; k++) { const d = await p.evaluate(() => window.__T().DEFER.done); if (d) break; await p.waitForTimeout(2000); }
  const tryTake = async (label, pickFn, story) => { const r = await p.evaluate(async ([pickSrc, story]) => { const W = window.__W(), T = window.__T(), G = W.G; const P = T.P; if (story != null) P.storyI = story;
      if (!G.onFoot) { T.toggleCar(); await new Promise(ok => setTimeout(ok, 1500)); }
      const tg = (0, eval)('(' + pickSrc + ')')(T, G); if (!tg) return { err: 'aucune cible' };
      G.me.x = tg.x + Math.cos(tg.h) * 2.4; G.me.z = tg.z - Math.sin(tg.h) * 2.4; await new Promise(ok => setTimeout(ok, 700));
      const help0 = (document.getElementById('help') || {}).textContent || ''; T.toggleCar(); await new Promise(ok => setTimeout(ok, 120)); const help1 = (document.getElementById('help') || {}).textContent || ''; await new Promise(ok => setTimeout(ok, 2400));
      const took = !G.onFoot; let moved = 0, y0 = null, y1 = null; if (took) { const c = G.car, x0 = c.x, z0 = c.z; y0 = c.jy; window.__auto = () => ({ fwd: 1, side: 0, brake: false }); let vm = 0; for (let i = 0; i < 25; i++) { await new Promise(ok => setTimeout(ok, 200)); vm = Math.max(vm, Math.abs(c.v)); } window.__vm = +vm.toFixed(1); window.__auto = () => ({ fwd: 0, side: 0, brake: true }); moved = Math.hypot(c.x - x0, c.z - z0); y1 = c.jy != null ? c.jy : T.GH(c.x, c.z); }
      return { took, kind: G.ride && G.ride.kind, famille: G.ride && G.ride.snd, max: G.ride && G.ride.def ? G.ride.def.max : null, vmax: window.__vm, moved: +moved.toFixed(1), yAvant: tg.y, yApres: y1 == null ? null : +y1.toFixed(2), msg: took ? '' : help1.slice(0, 120) }; }, [pickFn.toString(), story]); console.log(label, JSON.stringify(r)); return r; };
  const res = [];
  res.push(['parking ville', await tryTake('voiture garée (ville)', (T, G) => { const P3 = T.PARK3D.G.std; const s = P3.spots.filter(s => !s.taken && Math.abs(s.y - T.GH(s.x, s.z)) < 0.5); const sp = s[Math.floor(s.length / 3)]; return sp && { x: sp.x, z: sp.z, h: sp.ry, y: sp.y }; }), r => r.took && r.moved > 3]);
  res.push(['avenue Sud', await tryTake('voiture des avenues de Sud', (T, G) => { const q = (T.RDX.cars || []).find(q => q.m.visible && !q.frozen); return q && { x: q.m.position.x, z: q.m.position.z, h: q.m.rotation.y, y: q.m.position.y }; }), r => r.took && r.moved > 3]);
  res.push(['luxe Archipel (2 missions)', await tryTake('voiture de luxe de l\'Archipel, 2 missions', (T, G) => { const P3 = T.PARK3D.G.lux; if (!P3) return null; const sp = P3.spots.find(s => !s.taken); return sp && { x: sp.x, z: sp.z, h: sp.ry, y: sp.y }; }, 2), r => !r.took && /débloquent/.test(r.msg)]);
  res.push(['luxe Archipel (5 missions)', await tryTake('voiture de luxe de l\'Archipel, 5 missions', (T, G) => { const P3 = T.PARK3D.G.lux; if (!P3) return null; const sp = P3.spots.find(s => !s.taken); return sp && { x: sp.x, z: sp.z, h: sp.ry, y: sp.y }; }, 5), r => r.took]);
  let ok = 0; res.forEach(([n, r, f]) => { const g = f(r); if (g) ok++; console.log(n, g ? 'OK' : 'À CORRIGER'); });
  console.log(`BILAN voitures prises ${ok}/${res.length}`);
  console.log('ERR', errs.slice(0, 3).join(' | ') || 'none'); await b.close(); })().catch(e => { console.log('ERREUR', e.message.slice(0, 300)); process.exit(1); });
