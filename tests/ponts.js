// Usage : node tests/ponts.js <page-test.html> <save.json> <dossier captures> [filtre nom]
// Thomas 24/11 10h34 : « Quand on roule sur les ponts, on a les vues de dessous… Il faut que tu passes par tous les ponts… T'en laisses pas un seul sans exception. »
// Pour CHAQUE tablier (T.DK.decks) : on le roule de bout en bout au pilote automatique (vraie physique, vraie caméra), on note à chaque 1/10 s
//  · caméra sous le toit de la voiture (cam.y < voiture + 0,9 m) = VUE DE DESSOUS
//  · caméra sous la surface d'un tablier au-dessus d'elle (tablier entre 0 et 6 m au-dessus de la caméra, à sa verticale) = CAMÉRA SOUS LE TABLIER
//  · chute de plus de 1,5 m = CHUTE
// et on prend 5 captures par pont (20, 40, 60, 80 %, plus la pire image).
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')), out = process.argv[4], only = process.argv[5] || '';
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {} }, save);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 200)));
  await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 300; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.getClientRects().length && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + !!window.__zonesPretes; } catch (e) { return 'x'; } }); if (/^play\|true/.test(st) && k > 3) break; }
  for (let k = 0; k < 60; k++) { const st = await p.evaluate(() => { const G = window.__W().G; const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + (document.querySelector('.dveil') ? 'voile' : '') + '|' + Math.round(G.car.x) + ',' + Math.round(G.car.z); }); if (/^play\|\|/.test(st) && !/\|0,0$/.test(st)) break; await p.waitForTimeout(1000); }
  await p.evaluate(() => { const W = window.__W(), T = window.__T(), G = W.G; const g = document.getElementById('guide'); if (g) g.remove(); if (G.mode !== 'play') G.mode = 'play'; if (G.onFoot && G.parked) { G.inside = false; T.finishEnter({ own: true }); } document.querySelectorAll('#notes,.note-bar').forEach(e => e.style.display = 'none'); });
  await p.waitForTimeout(2000);
  const decks = await p.evaluate(() => window.__T().DK.decks.map((D, i) => { let L = 0; for (let k = 1; k < D.S.length; k++) L += Math.hypot(D.S[k][0] - D.S[k - 1][0], D.S[k][1] - D.S[k - 1][1]); return { i, name: D.name, n: D.S.length, L: Math.round(L), top: Math.max(...D.S.map(s => s[2])) }; }));
  console.log('TABLIERS', decks.length); decks.forEach(d => console.log(' ', d.i, d.name, d.L + ' m', 'haut ' + d.top.toFixed(1)));
  let bad = 0; const bilan = [];
  for (const d of decks) { if (only && !d.name.includes(only)) continue;
    const res = await p.evaluate(async (di) => { const G = window.__W().G, T = window.__T(), c = G.car, D = T.DK.decks[di], S = D.S; const a = S[0], b2 = S[Math.min(S.length - 1, 4)], h = Math.atan2(b2[0] - a[0], b2[1] - a[1]); const g0 = T.GH(a[0], a[1]);
      c.x = a[0] - Math.sin(h) * 14; c.z = a[1] - Math.cos(h) * 14; c.h = h; c.v = 8; c.jy = a[2] - g0 > 1.2 ? a[2] : null; c.jv = 0; c.air = 0; G.snapCam = true;
      if (c.jy != null) { c.x = a[0]; c.z = a[1]; }
      let bi0 = 0; window.__auto = () => { let bi = bi0, bd = 1e9; for (let i = Math.max(0, bi0 - 10); i < Math.min(S.length, bi0 + 40); i++) { const dd = (S[i][0] - c.x) ** 2 + (S[i][1] - c.z) ** 2; if (dd < bd) { bd = dd; bi = i; } } bi0 = bi; const tg = S[Math.min(S.length - 1, bi + 4)]; let df = Math.atan2(tg[0] - c.x, tg[1] - c.z) - c.h; while (df > Math.PI) df -= 2 * Math.PI; while (df < -Math.PI) df += 2 * Math.PI; return { fwd: Math.abs(c.v) > 22 ? 0 : 1, side: Math.max(-1, Math.min(1, -df * 2.5)), brake: false }; };
      window.__pl = { lg: [], done: false, prog: 0 }; const t0 = performance.now(), maxT = 20000 + D.S.length * 300;
      const iv = setInterval(() => { const cam = T.cam.position, cy = (c.jy != null ? c.jy : T.GH(c.x, c.z)); let over = null; for (const E of T.DK.decks) for (let k = 0; k < E.S.length; k += 1) { const s = E.S[k]; if (Math.abs(s[0] - cam.x) < (E.w || 10) / 2 + 1 && Math.abs(s[1] - cam.z) < (E.w || 10) / 2 + 1 && s[2] > cam.y && s[2] < cam.y + 6) { over = s[2]; break; } }
        const prog = bi0 / (S.length - 1); window.__pl.prog = prog; window.__pl.lg.push([+c.x.toFixed(1), +c.z.toFixed(1), +cy.toFixed(2), +cam.y.toFixed(2), over == null ? null : +over.toFixed(1), +prog.toFixed(3), +c.v.toFixed(1)]);
        if (prog > 0.985 || performance.now() - t0 > maxT) { clearInterval(iv); window.__pl.done = true; window.__auto = () => ({ fwd: 0, side: 0, brake: true }); } }, 100);
      return { start: [Math.round(c.x), Math.round(c.z)], onDeckStart: c.jy != null }; }, d.i);
    const marks = [0.2, 0.4, 0.6, 0.8]; let mi = 0, shots = [];
    for (let k = 0; k < 2000; k++) { await p.waitForTimeout(250); const st = await p.evaluate(() => ({ done: window.__pl.done, prog: window.__pl.prog })); if (mi < marks.length && st.prog >= marks[mi]) { const f = `${out}/${String(d.i).padStart(2, '0')}_${Math.round(marks[mi] * 100)}.png`; await p.screenshot({ path: f }); shots.push(f); mi++; } if (st.done) break; }
    const lg = await p.evaluate(() => window.__pl.lg);
    let under = 0, inDeck = 0, fall = 0, worst = null, wv = 0;
    for (let i = 0; i < lg.length; i++) { const r = lg[i]; const u = r[3] < r[2] + 0.9, dk = r[4] != null && r[4] > r[3] && r[4] - r[3] < 6 && r[4] > r[2] - 0.5; if (u) under++; if (dk) inDeck++; if (i && lg[i - 1][2] - r[2] > 1.5) fall++; const sc = (u ? r[2] + 0.9 - r[3] : 0) + (dk ? 3 : 0); if (sc > wv) { wv = sc; worst = r; } }
    const last = lg[lg.length - 1] || [0, 0, 0, 0, null, 0, 0]; const prog = last[5];
    if (worst) { await p.evaluate(([x, z]) => { const G = window.__W().G; }, worst); }
    const ok = !under && !inDeck && !fall && prog > 0.95; if (!ok) bad++;
    const line = `${d.i} ${d.name} (${d.L} m) : ${lg.length / 10} s, ${Math.round(prog * 100)} % roulé${under ? ' · VUE DE DESSOUS ' + under + ' images' : ''}${inDeck ? ' · CAMÉRA SOUS UN TABLIER ' + inDeck + ' images' : ''}${fall ? ' · CHUTES ' + fall : ''}${prog <= 0.95 ? ' · ARRÊTÉ à ' + last[0] + ',' + last[1] : ''}${worst ? ' · pire : voiture ' + worst[0] + ',' + worst[1] + ' y ' + worst[2] + ' caméra y ' + worst[3] + ' tablier dessus ' + worst[4] : ''} ${ok ? 'OK' : 'À CORRIGER'}`;
    console.log(line); bilan.push(line); fs.writeFileSync(`${out}/${String(d.i).padStart(2, '0')}.json`, JSON.stringify(lg));
  }
  console.log(`BILAN · ${decks.length} tabliers · à corriger : ${bad}`);
  console.log('ERR', errs.slice(0, 3).join(' | ') || 'none'); await b.close(); })().catch(e => { console.log('ERREUR', e.message.slice(0, 300)); process.exit(1); });
