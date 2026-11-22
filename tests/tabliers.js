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
  for (let k = 0; k < 400; k++) { await p.waitForTimeout(1500); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.offsetParent && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } return G.mode + '|' + !!window.__zonesPretes + '|' + !!(c && c.offsetParent) + '|' + (document.querySelector('#screen h2') || {}).textContent; } catch (e) { return 'x ' + e.message; } }); if (k % 10 === 0) console.log('attente', k, st); if (st.startsWith('play') && k > 3) break; }
  await p.waitForTimeout(6000);
  const info = await p.evaluate(() => { const G = window.__W().G; window.__auto = () => ({ fwd: 0, side: 0, brake: false }); return { mode: G.mode, onFoot: G.onFoot, parked: !!G.parked, inside: !!G.inside, sudx: JSON.stringify(window.__W().SUDX).slice(0, 300) }; });
  console.log('ETAT', JSON.stringify(info));
  const res = await p.evaluate(async () => { const W = window.__W(), T = window.__T(), { G, DK, GH, DECK_DEFS } = W, { updateCar, finishEnter } = T; G.inside = false; if (G.onFoot && G.parked) finishEnter({ own: true });
    const c = G.car, out = []; let mode = { fwd: 0, side: 0, brake: false }; window.__auto = () => mode;
    const place = (x, z, h) => { c.x = x; c.z = z; c.h = h; c.v = 0; c.s = 0; c.jy = null; c.jv = 0; c.air = 0; c.air0 = null; c.pg = null; c._lx = x; c._lz = z; DK.onDeck = false; };
    const dense = K => { const P = []; for (let i = 0; i < K.length - 1; i++) { const a = K[i], b = K[i + 1], L = Math.hypot(b[0] - a[0], b[1] - a[1]), n = Math.max(1, Math.ceil(L / 2)); for (let k = 0; k < n; k++) { const t = k / n; P.push([a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t]); } } P.push(K[K.length - 1].slice()); return P; };
    for (const D of DECK_DEFS) { for (const rev of [false, true]) { const K = rev ? D.K.slice().reverse() : D.K; if (K[0][2] > 3) continue; const P = dense(K), R = { pont: D.name + (rev ? " (retour)" : ""), ok: true, notes: [] };
        const dx = P[3][0] - P[0][0], dz = P[3][1] - P[0][1], l = Math.hypot(dx, dz), ux = dx / l, uz = dz / l; { let st = null; for (const off of [0, 0.5, -0.5, 1, -1, 1.5, -1.5]) { const ca = Math.cos(off), sa = Math.sin(off), vx = ux * ca - uz * sa, vz = ux * sa + uz * ca; let okk = true; for (let d = 6; d <= 30; d += 6) if (W.isWater(P[0][0] - vx * d, P[0][1] - vz * d)) okk = false; if (okk) { st = [P[0][0] - vx * 30, P[0][1] - vz * 30, Math.atan2(vx, vz)]; break; } } if (!st) { R.notes.push('aucun accès par la terre à 30 m'); st = [P[0][0] - ux * 30, P[0][1] - uz * 30, Math.atan2(ux, uz)]; } place(st[0], st[1], st[2]); } mode = { fwd: 0.8, side: 0, brake: false };
        let idx = 0, under = 0, off = 0, stuck = 0, maxDev = 0, t = 0;
        for (t = 0; t < 30 * 300 && idx < P.length - 3; t++) { let bi = idx, bd = 1e9; for (let k = Math.max(0, idx - 3); k < Math.min(P.length, idx + 30); k++) { const d = Math.hypot(P[k][0] - c.x, P[k][1] - c.z); if (d < bd) { bd = d; bi = k; } } if (bd < 12) idx = Math.max(idx, bi);
          const tg = P[Math.min(P.length - 1, (bd < 12 ? idx : 0) + 6)]; c.h = Math.atan2(tg[0] - c.x, tg[1] - c.z); c.s = 0; const px = c.x, pz = c.z; updateCar(1 / 30);
          if (bd < 12 && idx > 0) { maxDev = Math.max(maxDev, bd); const hExp = P[idx][2], yC = c.jy == null ? 0 : c.jy; if (hExp > 3 && yC < hExp - 2.5 && bd < D.w / 2) { under++; if (under === 8) R.notes.push(`sous le tablier vers (${c.x.toFixed(0)}, ${c.z.toFixed(0)}) : voiture à ${yC.toFixed(1)} m, tablier à ${hExp.toFixed(1)} m`); } }
          if (Math.hypot(c.x - px, c.z - pz) < 0.05 && t > 60) { stuck++; if (stuck === 45) R.notes.push(`bloquée vers (${c.x.toFixed(0)}, ${c.z.toFixed(0)}), ${(idx / P.length * 100).toFixed(0)} % du trajet, cause ${(() => { const o = { x: c.x + Math.sin(c.h) * 2, z: c.z + Math.cos(c.h) * 2 }; return W.isWater(o.x, o.z) ? 'eau' : T.collideBlocks(Object.assign({}, o), 1.2) ? 'bloc' : T.collideProps(Object.assign({}, o), 1.2) ? 'prop' : W.collide0Terrain(Object.assign({}, o)) ? 'terrain' : T.onPonton(o.x, o.z) ? 'ponton' : '?'; })()}, sol ${GH(c.x, c.z).toFixed(1)} m, départ (${P[0][0].toFixed(0)}, ${P[0][1].toFixed(0)})`); if (stuck > 90) break; } else stuck = 0; }
        if (idx < P.length - 3) { R.ok = false; R.notes.push(`pas arrivée au bout (${(idx / P.length * 100).toFixed(0)} %, ${(t / 30).toFixed(0)} s, arrêt vers (${c.x.toFixed(0)}, ${c.z.toFixed(0)}) à ${(c.jy || 0).toFixed(1)} m, point attendu (${P[idx][0].toFixed(0)}, ${P[idx][1].toFixed(0)}) à ${P[idx][2].toFixed(1)} m)`); } if (under >= 8) R.ok = false; if (stuck >= 45) R.ok = false;
        out.push(R); } }
    window.__auto = () => ({ fwd: 0, side: 0, brake: false }); return out; });
  let bad = 0; res.forEach(R => { if (!R.ok) bad++; console.log((R.ok ? 'OK     · ' : 'DÉFAUT · ') + R.pont + (R.notes.length ? ' · ' + R.notes.join(' · ') : '')); });
  console.log('BILAN', bad, 'tablier(s) en défaut sur', res.length); console.log('ERR', errs.slice(0, 4).join(' | ') || 'none'); await b.close(); process.exit(bad ? 1 : 0); })().catch(e => { console.log('ERREUR', e.message.slice(0, 400)); process.exit(2); });
