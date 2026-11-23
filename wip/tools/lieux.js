// Usage : node tests/lieux.js <page.html> <save.json> [zones séparées par des virgules]
// Tâche 2 ter c de l'expert jeu (Thomas, 22/11 16h14 : « Tous les lieux doivent marcher. »)
// Dans chaque zone : des points de départ au sol, 8 caps, la voiture roule 3 s plein gaz (simulation pas à pas de updateCar) :
//  · chaque arrêt brutal sans rien de visible devant (rayon à 0,6 m et 1,5 m du sol, 5 m devant) = MUR INVISIBLE
//  · arrêt au bord d'une eau qu'on voit = normal (noté « rivage »)
//  · au repos, sans aucune commande pendant 3 s, la voiture ne doit pas bouger de plus de 0,3 m (sinon VOITURE QUI PART SEULE)
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')), only = (process.argv[4] || '').split(',').filter(Boolean);
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 900, height: 600 } });
  await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 200)));
  await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 400; k++) { await p.waitForTimeout(1500); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.offsetParent && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } return G.mode + '|' + !!window.__zonesPretes + '|' + !!(c && c.offsetParent) + '|' + (document.querySelector('#screen h2') || {}).textContent; } catch (e) { return 'x ' + e.message; } }); if (k % 10 === 0) console.log('attente', k, st); if (/^(play|guide)\|true/.test(st) && k > 3) break; }
  await p.waitForTimeout(6000);
  const info = await p.evaluate(() => { const G = window.__W().G; { const g = document.getElementById('guide'); if (g) g.remove(); if (G.mode === 'guide') G.mode = 'play'; } window.__auto = () => ({ fwd: 0, side: 0, brake: false }); return { mode: G.mode, onFoot: G.onFoot, parked: !!G.parked, inside: !!G.inside, sudx: JSON.stringify(window.__W().SUDX).slice(0, 300), park: Object.keys(window.__W().PARK3D.G).join(','), sudbb: JSON.stringify((window.__W().PARK3D.G.sud || {}).bb), zp: !!window.__zonesPretes }; });
  console.log('ETAT', JSON.stringify(info));
  const res = await p.evaluate(async ([only, pied]) => { const W = window.__W(), X = window.__X(), T = window.__T(), { G, DK, GH, isWater, collide0Terrain, ARCH, AP, SUDX } = W, { scene } = X, { updateCar, collideCar, collideBlocks, collideProps, finishEnter, AP_OLD } = T, leaveApt = T.leaveApt;
    if (G.inside === 'apt' && leaveApt) { try { leaveApt(); } catch (e) {} } G.inside = false;
    if (!pied && G.onFoot && G.parked) finishEnter({ own: true }); if (pied && !G.onFoot) { try { T.toggleCar && T.toggleCar(); } catch (e) {} G.onFoot = true; } const me = G.me;
    const c = G.car, out = { zones: [] }, rc = new THREE.Raycaster(); rc.camera = window.__F().camera;
    const visible = o => { for (let q = o; q; q = q.parent) if (!q.visible) return false; const m = o.material; if (!m) return false; const ms = Array.isArray(m) ? m : [m]; return ms.some(mm => mm.visible !== false && !(mm.transparent && mm.opacity < 0.08) && mm.colorWrite !== false); };
    const seen = (x, y, z, h, far) => { const hits = []; for (const dy of [0.6, 1.5]) { rc.set(new THREE.Vector3(x, y + dy, z), new THREE.Vector3(Math.sin(h), 0, Math.cos(h))); rc.far = far; rc.near = 0; const I = rc.intersectObjects(scene.children, true).filter(i => visible(i.object) && !(T.carMesh && isAnc(T.carMesh, i.object))); if (I.length) hits.push((I[0].object.name || I[0].object.type) + '@' + I[0].distance.toFixed(1)); } return hits; };
    const isAnc = (a, o) => { for (let q = o; q; q = q.parent) if (q === a) return true; return false; };
    const place = (x, z, h) => { c.x = x; c.z = z; c.h = h; c.v = 0; c.s = 0; c.jy = null; c.jv = 0; c.air = 0; c.air0 = null; c.pg = null; c._lx = x; c._lz = z; DK.onDeck = false; };
    let mode = { fwd: 0, side: 0, brake: false }; window.__auto = () => mode;
    const A = ARCH, Z = {
      archipel: { box: [-2300, -700, -560, 1400], n: 70 },
      milliardaires: { box: [A.C[0] - 100, A.C[1] - 100, A.C[0] + 100, A.C[1] + 100], n: 30 },
      esplanade: { box: [AP_OLD.x0 - 40, AP_OLD.zg - 20, AP_OLD.x1 + 40, AP_OLD.z1 + 40], n: 50 },
      aeroport: { box: [AP.x0, AP.zg - 40, AP.x1, AP.z1], n: 50 },
      stade: SUDX && SUDX.st ? { box: [SUDX.st[0] - 160, SUDX.st[1] - 160, SUDX.st[0] + 160, SUDX.st[1] + 160], n: 30 } : null,
      mall: SUDX && SUDX.mall ? { box: [SUDX.mall[0] - 160, SUDX.mall[1] - 120, SUDX.mall[0] + 160, SUDX.mall[1] + 120], n: 30 } : null,
      sud: W.PARK3D && W.PARK3D.G.sud && W.PARK3D.G.sud.spots.length ? (S => { const xs = S.map(q => q.x), zs = S.map(q => q.z); return { box: [Math.min(...xs) - 20, Math.min(...zs) - 20, Math.max(...xs) + 20, Math.max(...zs) + 20], n: 60 }; })(W.PARK3D.G.sud.spots) : null };
    let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
    for (const name in Z) { const zz = Z[name]; if (!zz || (only.length && !only.includes(name))) continue; const [x0, z0, x1, z1] = zz.box; const R = { zone: name, points: 0, essais: 0, murs: [], rivages: 0, seules: [], chocs: 0 };
      for (let tries = 0; tries < zz.n * 40 && R.points < zz.n; tries++) { const x = x0 + rnd() * (x1 - x0), z = z0 + rnd() * (z1 - z0);
        if (isWater(x, z)) continue; place(x, z, 0); const t = { x, z, h: 0 }; collideCar(Object.assign(c, {}), 2.1); if (Math.hypot(c.x - x, c.z - z) > 0.05) continue; place(x, z, 0);
        R.points++;
        if (pied) { const putMe = (h) => { me.x = x; me.z = z; me.h = h; me.v = 0; me.jy = 0; me.vy = 0; me._lx = x; me._lz = z; }; putMe(0); mode = { fwd: 0, side: 0, brake: false }; for (let i = 0; i < 90; i++) T.updateMe(1 / 30); { const dr = Math.hypot(me.x - x, me.z - z); if (dr > 0.3) R.seules.push([+x.toFixed(1), +z.toFixed(1), +dr.toFixed(2)]); }
          for (let k = 0; k < 8; k++) { const h = k * Math.PI / 4; putMe(h); mode = { fwd: 1, side: 0, brake: false }; R.essais++; let slow = 0;
            for (let i = 0; i < 75; i++) { const px = me.x, pz = me.z, pv = me.v || 0, ph = me.h; T.updateMe(1 / 30); const d = Math.hypot(me.x - px, me.z - pz); if (d > 3) { R.sauts = R.sauts || []; R.sauts.push([+px.toFixed(1), +pz.toFixed(1), +me.x.toFixed(1), +me.z.toFixed(1)]); break; }
              if (pv > 6 && d < pv / 30 * 0.25) slow++; else slow = 0;
              if (slow >= 5) { const gy = GH(px, pz); if (seen(px, gy, pz, ph, 2.5).length) { R.chocs++; break; } { const ax = px + Math.sin(ph) * 0.9, az = pz + Math.cos(ph) * 0.9, SB = W.SUDB, L = SB.map.get(Math.floor(ax / SB.cell) + ',' + Math.floor(az / SB.cell)) || []; if (L.some(b => { const dx = ax - b[0], dz = az - b[1], c = Math.cos(b[4]), s = Math.sin(b[4]); return Math.abs(dx * c - dz * s) < b[2] + 0.7 && Math.abs(dx * s + dz * c) < b[3] + 0.7; })) { R.objets = (R.objets || 0) + 1; break; } if (az > AP.z1 - 3 && Math.abs(ax) < AP.x1) { R.quais = (R.quais || 0) + 1; break; } } R.murs.push({ x: +px.toFixed(1), z: +pz.toFixed(1), cap: k * 45, gh: +gy.toFixed(2), eau: isWater(px + Math.sin(ph) * 1.5, pz + Math.cos(ph) * 1.5), blk: (() => { const o = { x: px + Math.sin(ph) * 0.8, z: pz + Math.cos(ph) * 0.8 }; return collideBlocks(o, 0.6) ? 'bloc' : collideProps(o, 0.6) ? 'prop' : collide0Terrain(o) ? 'terrain' : '?'; })() }); break; } } }
          continue; }
        // au repos 3 s
        mode = { fwd: 0, side: 0, brake: false }; for (let i = 0; i < 90; i++) updateCar(1 / 30); const dr = Math.hypot(c.x - x, c.z - z); if (dr > 0.3) R.seules.push([+x.toFixed(1), +z.toFixed(1), +dr.toFixed(2)]);
        for (let k = 0; k < 8; k++) { const h = k * Math.PI / 4; place(x, z, h); mode = { fwd: 1, side: 0, brake: false }; R.essais++;
          for (let i = 0; i < 90; i++) { const px = c.x, pz = c.z, pv = c.v, ph = c.h; updateCar(1 / 30); { const jump = Math.hypot(c.x - px, c.z - pz); if (jump > 3) { R.sauts = R.sauts || []; R.sauts.push([+px.toFixed(1), +pz.toFixed(1), +c.x.toFixed(1), +c.z.toFixed(1)]); break; } }
            if (pv > 6 && c.v < pv * 0.5) { const ahead = 3.5, ax = px + Math.sin(ph) * ahead, az = pz + Math.cos(ph) * ahead, nx = px + Math.sin(ph) * pv / 30 * 2, nz = pz + Math.cos(ph) * pv / 30 * 2; if (isWater(ax, az) || isWater(nx, nz)) { R.rivages++; break; } if (T.onPonton(nx, nz) || T.onPonton(ax, az)) { R.pontons = (R.pontons || 0) + 1; break; }
              const gy = GH(px, pz), vis = seen(px, gy, pz, ph, 5.5); if (vis.length) { R.chocs++; break; }
              R.murs.push({ x: +px.toFixed(1), z: +pz.toFixed(1), cap: k * 45, v: +pv.toFixed(1), gh: +gy.toFixed(2), deck: DK.onDeck, blk: (() => { const o = { x: ax, z: az }; return collideBlocks(o, 1.2) ? 'bloc' : collideProps(o, 1.2) ? 'prop' : collide0Terrain(o) ? 'terrain' : '?'; })() }); break; } } }
      }
      out.zones.push(R); }
    window.__auto = () => ({ fwd: 0, side: 0, brake: false }); return out; }, [only, !!process.env.PIED]);
  let tot = 0; for (const R of res.zones) { tot += R.murs.length + R.seules.length + (R.sauts || []).length; console.log(`${R.murs.length || R.seules.length || (R.sauts || []).length ? 'DÉFAUT' : 'OK    '} · ${R.zone} · ${R.points} points, ${R.essais} trajets · murs invisibles ${R.murs.length} · voiture qui part seule ${R.seules.length} · sauts ${(R.sauts || []).length} · chocs visibles ${R.chocs} · rivages ${R.rivages} · pontons ${R.pontons || 0} · objets ${R.objets || 0} · quais ${R.quais || 0}`);
    R.murs.slice(0, 15).forEach(m => console.log('   mur', JSON.stringify(m))); R.seules.slice(0, 10).forEach(m => console.log('   seule', JSON.stringify(m))); (R.sauts || []).slice(0, 10).forEach(m => console.log('   saut', JSON.stringify(m))); }
  fs.writeFileSync('/tmp/pc/lieux.json', JSON.stringify(res));
  console.log('BILAN', tot, 'défaut(s)'); console.log('ERR', errs.slice(0, 4).join(' | ') || 'none'); await b.close(); process.exit(tot ? 1 : 0); })().catch(e => { console.log('ERREUR', e.message.slice(0, 400)); process.exit(2); });
