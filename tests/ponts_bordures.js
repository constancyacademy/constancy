// tests/ponts_bordures.js · V310.128 (file de nuit du 27/11, tâche 1, R1 R2) · Usage : node tests/ponts_bordures.js <page.html> <save.json>
// Pour chaque tablier (DECK_DEFS, les 2 sens) : la voiture roule au centre jusqu'à 40 % du pont, puis on la braque vers la bordure gauche puis droite, à 10° et 30°, plein gaz pendant 3 s (simulation image par image : updateCar + updateDecks)
//  · CHUTE si la voiture finit plus de 2,5 m sous le tablier alors qu'elle est dans son emprise, ou hors de l'emprise et sous le tablier
//  · ARRÊT si la vitesse tombe sous 20 % de la vitesse d'entrée à 10° (sous 10 % à 30°)
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')), only = (process.argv[4] || '').split(',').filter(Boolean);
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 900, height: 600 } });
  await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 200)));
  await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 400; k++) { await p.waitForTimeout(1500); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.offsetParent && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + !!window.__zonesPretes + '|' + !!(c && c.offsetParent) + '|' + (document.querySelector('#screen h2') || {}).textContent; } catch (e) { return 'x ' + e.message; } }); if (k % 10 === 0) console.log('attente', k, st); if (/^(play|guide)\|true/.test(st) && k > 3) break; }
  for (let k = 0; k < 60; k++) { const st = await p.evaluate(() => { const G = window.__W().G; const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + (document.querySelector('.dveil') ? 'voile' : '') + '|' + Math.round(G.car.x) + ',' + Math.round(G.car.z); }); if (/^(play|guide)\|\|/.test(st) && !/\|0,0$/.test(st)) break; await p.waitForTimeout(1000); } /* V310.36 : « Continuer » passe par le voile, puis le guide du retour */
  await p.waitForTimeout(6000);
  const info = await p.evaluate(() => { const G = window.__W().G; window.__auto = () => ({ fwd: 0, side: 0, brake: false }); return { mode: G.mode, onFoot: G.onFoot, parked: !!G.parked, inside: !!G.inside, sudx: JSON.stringify(window.__W().SUDX).slice(0, 300) }; });
  console.log('ETAT', JSON.stringify(info));
  const res = await p.evaluate(async () => { const W = window.__W(), T = window.__T(), { G, DK, GH, DECK_DEFS } = W, { updateCar, finishEnter } = T; G.inside = false; if (G.onFoot && G.parked) finishEnter({ own: true });
    const c = G.car, out = []; let mode = { fwd: 0, side: 0, brake: false }; window.__auto = () => mode;
    const place = (x, z, h) => { c.x = x; c.z = z; c.h = h; c.v = 0; c.s = 0; c.jy = null; c.jv = 0; c.air = 0; c.air0 = null; c.pg = null; c._lx = x; c._lz = z; DK.onDeck = false; };
    const dense = K => { const P = []; for (let i = 0; i < K.length - 1; i++) { const a = K[i], b = K[i + 1], L = Math.hypot(b[0] - a[0], b[1] - a[1]), n = Math.max(1, Math.ceil(L / 2)); for (let k = 0; k < n; k++) { const t = k / n; P.push([a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t]); } } P.push(K[K.length - 1].slice()); return P; };
    { const gd = document.getElementById('guide'); if (gd) gd.remove(); } G.mode = 'play'; G.mission = null; const UD = W.updateDecks; if (!UD) return [{ pont: 'updateDecks absent de __W', ok: false, notes: [] }];
    const keys = ['x', 'z', 'h', 'v', 's', 'jy', 'jv', 'air', 'air0', 'pg', '_lx', '_lz'];
    for (const D of DECK_DEFS) { for (const rev of [false, true]) { const K = rev ? D.K.slice().reverse() : D.K; if (K[0][2] > 3) continue; const P = dense(K), R = { pont: D.name + (rev ? " (retour)" : ""), ok: true, notes: [] };
        const dx = P[3][0] - P[0][0], dz = P[3][1] - P[0][1], l = Math.hypot(dx, dz), ux = dx / l, uz = dz / l; let st = null; for (const off of [0, 0.5, -0.5, 1, -1, 1.5, -1.5]) { const ca = Math.cos(off), sa = Math.sin(off), vx = ux * ca - uz * sa, vz = ux * sa + uz * ca; let okk = true; for (let d = 6; d <= 30; d += 6) if (W.isWater(P[0][0] - vx * d, P[0][1] - vz * d)) okk = false; if (okk) { st = [P[0][0] - vx * 30, P[0][1] - vz * 30]; break; } } if (!st) st = [P[0][0] - ux * 30, P[0][1] - uz * 30];
        place(st[0], st[1], Math.atan2(P[0][0] - st[0], P[0][1] - st[1])); mode = { fwd: 1, side: 0, brake: false };
        let idx = 0, t = 0; const goal = Math.floor(P.length * 0.4);
        for (t = 0; t < 30 * 120 && idx < goal; t++) { let bi = idx, bd = 1e9; for (let k = Math.max(0, idx - 3); k < Math.min(P.length, idx + 30); k++) { const d = Math.hypot(P[k][0] - c.x, P[k][1] - c.z); if (d < bd) { bd = d; bi = k; } } if (bd < 12) idx = Math.max(idx, bi);
          const tg = P[Math.min(P.length - 1, (bd < 12 ? idx : 0) + 6)]; c.h = Math.atan2(tg[0] - c.x, tg[1] - c.z); c.s = 0; updateCar(1 / 30); UD(1 / 30); }
        if (idx < goal) { R.ok = false; R.notes.push('pas arrivé à 40 % au centre'); out.push(R); continue; }
        const snap = {}; keys.forEach(k => snap[k] = c[k]); const onD = DK.onDeck, a = P[idx], bq = P[Math.min(P.length - 1, idx + 1)], th = Math.atan2(bq[0] - a[0], bq[1] - a[1]);
        for (const side of [-1, 1]) for (const ang of [10, 30]) { keys.forEach(k => c[k] = snap[k]); DK.onDeck = onD; c.h = th + side * ang * Math.PI / 180; const v0 = Math.max(8, Math.abs(c.v)); let vmin = 1e9, fell = null;
          for (let f = 0; f < 90; f++) { c.s = 0; updateCar(1 / 30); UD(1 / 30); vmin = Math.min(vmin, Math.abs(c.v));
            let bd = 1e9, hh = 0; for (let k = Math.max(0, idx - 10); k < Math.min(P.length, idx + 60); k++) { const d = Math.hypot(P[k][0] - c.x, P[k][1] - c.z); if (d < bd) { bd = d; hh = P[k][2]; } } const y = c.jy == null ? 0 : c.jy;
            if (!fell && hh > 3 && y < hh - 2.5) fell = `(${c.x.toFixed(0)}, ${c.z.toFixed(0)}) à ${y.toFixed(1)} m, tablier ${hh.toFixed(1)} m, écart ${bd.toFixed(1)} m`; }
          const lim = ang === 10 ? 0.2 : 0.1; if (fell) { R.ok = false; R.notes.push(`CHUTE ${side < 0 ? 'gauche' : 'droite'} ${ang}° ${fell}`); } else if (vmin < v0 * lim) { R.ok = false; R.notes.push(`ARRÊT ${side < 0 ? 'gauche' : 'droite'} ${ang}° (${vmin.toFixed(1)} sur ${v0.toFixed(1)} m/s)`); } else R.notes.push(`${side < 0 ? 'G' : 'D'}${ang}° ${Math.round(vmin / v0 * 100)} %`); }
        out.push(R); } }
    window.__auto = () => ({ fwd: 0, side: 0, brake: false }); return out; });
  let bad = 0; res.forEach(R => { if (!R.ok) bad++; console.log((R.ok ? 'OK     · ' : 'DÉFAUT · ') + R.pont + (R.notes.length ? ' · ' + R.notes.join(' · ') : '')); });
  console.log('BILAN', bad, 'tablier(s) en défaut sur', res.length, '(bordures gauche et droite à 10° et 30°)'); console.log('ERR', errs.slice(0, 4).join(' | ') || 'none'); await b.close(); process.exit(bad ? 1 : 0); })().catch(e => { console.log('ERREUR', e.message.slice(0, 400)); process.exit(2); });
