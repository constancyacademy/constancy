// Usage : NODE_PATH=<node_modules> node tests/couleurs.js <index.html> [chemin de chromium] · bilan « modèle · couleurs OK » (tâche 2 bis de l'expert jeu, 22/11)
// Aucun objet blanc (Thomas, 22/11 16h05 : « Tu retournes le jeu dans tous les sens »). Après window.__zonesPretes (avec ?alldino=1),
// on contrôle chaque modèle chargé (MODELS[*].proto) et toute la scène : Toute couleur de sommets doit être en Float32, 3 composantes,
// non entrelacée, valeur maximale 1 au plus pour les modèles (1,5 pour les décors faits par le jeu, qui éclaircissent parfois exprès jusqu'à 1,1) (sinon : octets compressés lus bruts = blanc saturé, cause des voitures blanches de V310.13).
// Et aucun modèle « vc » ne doit avoir plus de 90 % de ses sommets au-dessus de 0,95 sur les 3 canaux (blanc saturé), sauf ceux marqués white: true.
const { chromium } = require('playwright'); const path = require('path');
(async () => { const page = path.resolve(process.argv[2]), exe = process.argv[3] || '/opt/pw-browsers/chromium';
  const b = await chromium.launch({ executablePath: exe, args: ['--allow-file-access-from-files', '--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 800, height: 600 }, deviceScaleFactor: 1 });
  await ctx.addInitScript(() => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); });
  if (process.env.SERVE_THREE) { const P = process.env.SERVE_THREE; await ctx.route(/^https?:/, r => { const u = r.request().url(); if (/three\.min\.js/.test(u)) return r.fulfill({ path: P + '/build/three.min.js', contentType: 'application/javascript' }); if (/three@0\.128\.0\/examples\/js\//.test(u)) return r.fulfill({ path: P + '/examples/js/' + u.split('examples/js/')[1], contentType: 'application/javascript' }); if (/localhost/.test(u)) return r.continue(); return r.abort(); }); }
  else await ctx.route(/^https?:/, r => r.abort());
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 160)));
  const url = /^https?:/.test(process.argv[2]) ? process.argv[2] : 'file://' + page; await p.goto(url + (url.includes('?') ? '&' : '?') + 'nostat=1&autostart=1&alldino=1');
  await p.waitForFunction(() => window.__zonesPretes === true, null, { timeout: 900000 }).catch(() => console.log('ATTENTION · __zonesPretes jamais vrai, contrôle sur ce qui est chargé'));
  let n0 = -1; for (let k = 0; k < 40; k++) { const n = await p.evaluate(() => Object.keys(window.__W().MODELS).length); if (n === n0 && k > 4) break; n0 = n; await p.waitForTimeout(3000); }
  const res = await p.evaluate(() => { const W = window.__W(), out = [], seen = new Set(), src = document.documentElement.innerHTML;
    const white = k => new RegExp('\\b' + k + ':\\s*\\{[^}]*white:\\s*true').test(src), vc = k => new RegExp('\\b' + k + ':\\s*\\{[^}]*vc:\\s*true').test(src);
    const geoCheck = g => { const c = g && g.attributes && g.attributes.color; if (!c) return null; const A = c.array, n = c.count; if (!c.isInterleavedBufferAttribute && A.length < n * c.itemSize) return null; /* tableau libéré après l'envoi à la carte graphique (économie de mémoire du jeu) : déjà contrôlé dans MODELS */ let max = 0, sat = 0;
      const typeOk = A instanceof Float32Array && c.itemSize === 3 && !c.isInterleavedBufferAttribute;
      let nan = 0; for (let i = 0; i < n; i++) { const r = c.getX(i), gg = c.getY(i), bb = c.getZ(i); if (r !== r || gg !== gg || bb !== bb) { nan++; continue; } max = Math.max(max, r, gg, bb); if (r > 0.95 && gg > 0.95 && bb > 0.95) sat++; }
      return { typeOk: typeOk && !nan, type: A.constructor.name + '/' + c.itemSize + (c.normalized ? 'n' : '') + (nan ? ' · ' + nan + ' sommets NaN sur ' + n : ''), max, sat, n }; };
    const checkObj = (label, root, isVc, isWhite) => { let tot = 0, sat = 0, max = 0, bad = []; root.traverse(o => { if (!o.isMesh || !o.geometry) return; const r = geoCheck(o.geometry); if (!r) return; seen.add(o.geometry.uuid); tot += r.n; sat += r.sat; max = Math.max(max, r.max); if (!r.typeOk) bad.push('type ' + r.type); if (r.max > 1.0001) bad.push('max ' + r.max.toFixed(2)); });
      if (!tot) return; const fr = sat / tot; if (isVc && !isWhite && fr > 0.9) bad.push('blanc saturé ' + Math.round(fr * 100) + ' %');
      out.push({ v: label, n: tot, max: +max.toFixed(3), blanc: Math.round(fr * 100), ok: !bad.length, note: [...new Set(bad)].join(' ; ') }); };
    Object.keys(W.MODELS).forEach(k => { const m = W.MODELS[k]; if (m && m.proto) checkObj('modèle ' + k, m.proto, vc(k), white(k)); });
    // toute la scène (décors fusionnés, chargeurs à part : avatars, lots tardifs, véhicules à part, veg_palm.json)
    let sTot = 0, sBad = []; W.scene.traverse(o => { if (!o.isMesh || !o.geometry || seen.has(o.geometry.uuid)) return; const r = geoCheck(o.geometry); if (!r) return; seen.add(o.geometry.uuid); sTot++; if (!r.typeOk || !(r.max <= 1.5)) sBad.push((o.name || o.parent && o.parent.name || 'sans nom') + ' (' + r.type + ', max ' + r.max.toFixed(2) + ')'); });
    out.push({ v: 'scène · ' + sTot + ' géométries colorées hors MODELS', ok: !sBad.length, note: sBad.slice(0, 12).join(' ; ') + (sBad.length > 12 ? ' … +' + (sBad.length - 12) : '') });
    return out; });
  res.forEach(x => console.log((x.ok ? 'OK    ' : 'DÉFAUT') + ' · ' + x.v + (x.n != null ? ' · sommets ' + x.n + ' · max ' + x.max + ' · blanc ' + x.blanc + ' %' : '') + (x.note ? ' · ' + x.note : '')));
  console.log('BILAN', res.filter(x => x.ok).length, 'OK ·', res.filter(x => !x.ok).length, 'DÉFAUT');
  console.log('ERR', errs.slice(0, 6).join(' || ') || 'none'); await b.close(); process.exit(res.some(x => !x.ok) ? 1 : 0); })().catch(e => { console.log('ERREUR', e.message.slice(0, 300)); process.exit(2); });
