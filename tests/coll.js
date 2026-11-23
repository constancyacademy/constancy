// Voiture collée contre une autre (Thomas 23/11 15h36) : on se place flanc contre flanc d'une voiture du trafic arrêtée, plein gaz tout droit 3 s, puis marche arrière 2 s. Il faut repartir.
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); window.__norender = 1; try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 200)));
  await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 200; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.getClientRects().length && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + !!window.__zonesPretes; } catch (e) { return 'x'; } }); if (/^(play|guide)\|true/.test(st) && k > 3) break; }
  await p.evaluate(() => { const W = window.__W(), T = window.__T(), G = W.G; const g = document.getElementById('guide'); if (g) g.remove(); if (G.mode !== 'play') G.mode = 'play'; if (G.onFoot && G.parked) { G.inside = false; T.finishEnter({ own: true }); } });
  await p.waitForTimeout(3000);
  const out = [];
  for (const [nom, side, fwd, dur] of [['flanc-avant', 1, 1, 3000], ['flanc-arriere', 1, -1, 2500], ['nez-contre-arriere-recule', 0, -1, 2500]]) {
    const r0 = await p.evaluate(([side]) => { const W = window.__W(), G = W.G, tr = W.traffic || window.__T().traffic; const L = window.__T().traffic || []; let a = L.find(q => q.mesh && q.mesh.visible && !q.bus && Math.hypot(q.x - G.car.x, q.z - G.car.z) < 400) || L.find(q => q.mesh && !q.bus); if (!a) return null; a.frozen = true; a.speed = 0; const fx = Math.sin(a.h), fz = Math.cos(a.h), rx = Math.cos(a.h), rz = -Math.sin(a.h);
      if (side) { G.car.x = a.x + rx * 2.0; G.car.z = a.z + rz * 2.0; } else { G.car.x = a.x - fx * 3.2; G.car.z = a.z - fz * 3.2; } G.car.h = a.h; G.car.v = 0; G.car._lx = G.car.x; G.car._lz = G.car.z; window.__A = a; return { x: G.car.x, z: G.car.z }; }, [side]);
    if (!r0) { out.push(nom + ' : pas de voiture du trafic'); continue; }
    await p.evaluate(f => { window.__auto = () => ({ fwd: f, side: 0, brake: false }); }, fwd);
    await p.waitForTimeout(dur);
    const r1 = await p.evaluate(() => { const G = window.__W().G; window.__auto = () => ({ fwd: 0, side: 0, brake: true }); if (window.__A) window.__A.frozen = false; return { x: G.car.x, z: G.car.z, v: G.car.v }; });
    const d = Math.hypot(r1.x - r0.x, r1.z - r0.z); out.push(`${nom} : ${d.toFixed(1)} m en ${dur / 1000} s ${d > 6 ? 'OK' : 'COLLÉ'}`); await p.waitForTimeout(800); }
  out.forEach(l => console.log(l)); console.log('ERR', errs.slice(0, 3).join(' | ') || 'none'); await b.close(); })().catch(e => { console.log('ERREUR', e.message.slice(0, 300)); process.exit(1); });
