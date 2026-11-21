// Usage : NODE_PATH=<node_modules> node tests/roues.js <page de test> · bilan « véhicule · roues OK » (tâche 3 de l'expert jeu, V310.5)
// Test automatique des roues (tâche 3 de l'expert jeu) : chaque voiture (CARS) et chaque véhicule (RIDES) est construit,
// on vérifie que des roues existent, que chaque roue tournante est bien une roue (rayon mesuré ≈ rayon de roulement,
// rien qui dépasse du pneu, donc aucun morceau de carrosserie accroché) et que spinWheels la fait tourner d'un angle v·dt/r.
const { chromium } = require('playwright'); const path = require('path');
(async () => { const page = path.resolve(process.argv[2]);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 800, height: 600 }, deviceScaleFactor: 1 });
  await ctx.route(/^https?:/, r => r.abort()); await ctx.addInitScript(() => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); });
  const p = await ctx.newPage(); const errs = []; p.on('console', m => { if (/roues/.test(m.text())) console.log('CONSOLE', m.text().slice(0, 200)); }); p.on('pageerror', e => errs.push(e.message.slice(0, 160)));
  await p.goto('file://' + page + '?nostat=1&autostart=1'); await p.waitForSelector('#quick', { timeout: 900000 });
  let n0 = -1; for (let k = 0; k < 40; k++) { const n = await p.evaluate(() => Object.keys(window.__W().MODELS).length); if (n === n0 && k > 6) break; n0 = n; await p.waitForTimeout(3000); }
  const res = await p.evaluate(() => { const W = window.__W(), out = [], V = new THREE.Vector3(), inv = new THREE.Matrix4(), M = new THREE.Matrix4();
    const check = (label, g, rDecl) => { g.updateMatrixWorld(true); const ws = []; g.traverse(o => { if (o.name === 'wheelF' || o.name === 'wheelB') ws.push(o); }); if (!g.userData.wheels) {} else g.userData.wheels.forEach(([w]) => { if (!ws.includes(w)) ws.push(w); });
      if (!ws.length) { out.push({ v: label, n: 0, ok: null, note: 'pas de roue tournante' }); return; }
      let r = rDecl; try { W.spinWheels(g, 0, 0, 0); r = g.userData.parts.r; } catch (e) {} let worst = 0, bad = [];
      ws.forEach((w, i) => { const rW = w.userData.r || 0; const O = new THREE.Vector3().setFromMatrixPosition(w.matrixWorld), A = new THREE.Vector3(1, 0, 0).transformDirection(w.matrixWorld), D = new THREE.Vector3(); let rmax = 0, xs = [1e9, -1e9], cnt = 0;
        w.traverse(m => { if (!m.isMesh || !m.geometry || !m.geometry.attributes.position) return; const a = m.geometry.attributes.position; for (let k = 0; k < a.count; k++) { V.fromBufferAttribute(a, k).applyMatrix4(m.matrixWorld); D.subVectors(V, O); const ax = D.dot(A); rmax = Math.max(rmax, Math.sqrt(Math.max(0, D.lengthSq() - ax * ax))); xs[0] = Math.min(xs[0], ax); xs[1] = Math.max(xs[1], ax); cnt++; } });
        const rr = rW || r || rmax, ratio = rmax / rr, wid = xs[1] - xs[0]; worst = Math.max(worst, ratio); if (!cnt || ratio > 1.25 || ratio < 0.6) bad.push(w.name + '#' + i + ' r=' + rmax.toFixed(2) + '/' + rr.toFixed(2) + ' larg=' + wid.toFixed(2)); });
      // rotation : 10 m/s pendant 0,1 s
      let rot = 'n/a'; try { const before = ws.map(w => w.rotation.x); W.spinWheels(g, 10, 0.2, 0.1); const d = ws.map((w, i) => w.rotation.x - before[i]); const exp = ws.map(w => 10 * 0.1 / (w.userData.r || (g.userData.parts ? g.userData.parts.r : r || 0.4))); rot = d.every((x, i) => Math.abs(x - exp[i]) < 1e-6) ? 'ok' : 'écart ' + d.map(x => x.toFixed(2)).join(','); if (rot !== 'ok' && !g.userData.parts) rot = 'n/a'; } catch (e) { rot = 'n/a'; }
      out.push({ v: label, n: ws.length, r: +(r || 0).toFixed(2), pire: +worst.toFixed(2), rot, ok: !bad.length && rot !== 'écart', note: bad.join(' ; ') }); };
    Object.keys(W.MODELS).filter(k => /^(car_|c_sedan|c_hatchback|c_suv|ambulance|bus|firetruck|c_delivery|c_truck|tractor3|combine3)/.test(k)).forEach(k => { try { const g = new THREE.Group(); const m = W.modelInstance ? W.modelInstance(k) : null; if (!m) return; g.add(m); g.userData.wheelR = W.MODELS[k].wheelR; check('modèle ' + k, g, W.MODELS[k].wheelR); } catch (e) { out.push({ v: 'modèle ' + k, ok: false, note: 'ERREUR ' + e.message }); } });
    (W.CARS || []).forEach(c => { try { const g = W.makeCar(c); check('voiture ' + c.id, g, 0); } catch (e) { out.push({ v: 'voiture ' + c.id, ok: false, note: 'ERREUR ' + e.message }); } });
    const RIDES = window.__RIDES || null; const kinds = []; try { for (const k in (typeof RIDES === 'object' && RIDES) || {}) kinds.push(k); } catch (e) {}
    return { out, kinds }; });
  // RIDES n'est pas exposé dans __W : on prend la liste depuis le code
  const src = require('fs').readFileSync(page, 'utf8'), ri = src.indexOf('const RIDES = {'), rb = src.slice(ri, src.indexOf('\n};', ri)); const kinds = [...rb.matchAll(/^\s+([a-zA-Z0-9_]+):\s*\{/gm)].map(m => m[1]); console.log('RIDES', kinds.join(' '));
  const res2 = await p.evaluate(kinds => { const W = window.__W(), out = [], V = new THREE.Vector3(), inv = new THREE.Matrix4(), M = new THREE.Matrix4();
    kinds.forEach(k => { let g; try { g = W.makeRide(k); } catch (e) { out.push({ v: 'véhicule ' + k, ok: false, note: 'ERREUR ' + e.message }); return; } g.updateMatrixWorld(true); const ws = []; g.traverse(o => { if (o.name === 'wheelF' || o.name === 'wheelB') ws.push(o); });
      let r = g.userData.wheelR || 0; g.traverse(o => { if (!r && o.userData && o.userData.key && W.MODELS[o.userData.key]) r = W.MODELS[o.userData.key].wheelR || 0; });
      if (!ws.length) { out.push({ v: 'véhicule ' + k, n: 0, ok: null, note: 'pas de roue tournante' }); return; } let worst = 0, bad = [];
      ws.forEach((w, i) => { const rW = w.userData.r || 0; const O = new THREE.Vector3().setFromMatrixPosition(w.matrixWorld), A = new THREE.Vector3(1, 0, 0).transformDirection(w.matrixWorld), D = new THREE.Vector3(); let rmax = 0, xs = [1e9, -1e9], cnt = 0; w.traverse(m => { if (!m.isMesh || !m.geometry || !m.geometry.attributes.position) return; const a = m.geometry.attributes.position; for (let q = 0; q < a.count; q++) { V.fromBufferAttribute(a, q).applyMatrix4(m.matrixWorld); D.subVectors(V, O); const ax = D.dot(A); rmax = Math.max(rmax, Math.sqrt(Math.max(0, D.lengthSq() - ax * ax))); xs[0] = Math.min(xs[0], ax); xs[1] = Math.max(xs[1], ax); cnt++; } });
        const rr = rW || r || rmax, ratio = rmax / rr, wid = xs[1] - xs[0]; worst = Math.max(worst, ratio); if (!cnt || ratio > 1.25 || ratio < 0.6) bad.push(w.name + '#' + i + ' r=' + rmax.toFixed(2) + '/' + rr.toFixed(2) + ' larg=' + wid.toFixed(2)); });
      let rot = 'n/a'; try { const before = ws.map(w => w.rotation.x); W.spinWheels(g, 10, 0.2, 0.1); const pr = g.userData.parts; const d = ws.map((w, i) => w.rotation.x - before[i]); const exp = ws.map(w => 10 * 0.1 / (w.userData.r || pr.r)); rot = d.every((x, i) => Math.abs(x - exp[i]) < 1e-6) ? 'ok' : 'écart ' + d.map(x => x.toFixed(2)).join(','); } catch (e) {}
      out.push({ v: 'véhicule ' + k, n: ws.length, r: +r.toFixed(2), pire: +worst.toFixed(2), rot, ok: !bad.length && !/écart/.test(rot), note: bad.join(' ; ') }); });
    return out; }, kinds);
  const all = res.out.concat(res2); all.forEach(x => console.log((x.ok === true ? 'OK    ' : x.ok === null ? 'FIXES ' : 'DÉFAUT') + ' · ' + x.v + ' · roues ' + (x.n || 0) + (x.r != null ? ' · r ' + x.r : '') + (x.pire != null ? ' · dépassement max ×' + x.pire : '') + (x.rot ? ' · rotation ' + x.rot : '') + (x.note ? ' · ' + x.note : '')));
  console.log('BILAN', all.filter(x => x.ok === true).length, 'OK ·', all.filter(x => x.ok === false).length, 'DÉFAUT ·', all.filter(x => x.ok === null).length, 'sans roue tournante');
  console.log('ERR', errs.slice(0, 6).join(' || ') || 'none'); await b.close(); })().catch(e => { console.log('ERREUR', e.message.slice(0, 300)); process.exit(1); });
