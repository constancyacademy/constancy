// Vidéo promo paysage en temps virtuel (30 i/s exactes) : node promovid.js page.html save.json outdir '[[nom,x,z,cap,heure,secondes,avance,braque],...]'
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), save = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')), out = process.argv[4]; fs.mkdirSync(out, { recursive: true });
  const SEGS = JSON.parse(process.argv[5]); const W0 = +(process.env.W || 1280), H0 = +(process.env.H || 720);
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: W0, height: H0 }, deviceScaleFactor: 1 });
  await ctx.route(/^https?:/, r => r.abort());
  await ctx.addInitScript(s => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); try { if (!sessionStorage.getItem('lx')) { for (const k in s) localStorage.setItem(k, s[k]); sessionStorage.setItem('lx', '1'); } } catch (e) {}
    const rr = window.requestAnimationFrame.bind(window), pn = performance.now.bind(performance); let q = []; window.__vtNow = 0;
    window.requestAnimationFrame = cb => { if (window.__vt) { q.push(cb); return q.length; } return rr(cb); };
    performance.now = () => window.__vt ? window.__vtNow : pn();
    window.__vtOn = () => { window.__vtNow = pn(); window.__vt = 1; window.__virtOn = 1; };
    window.__vtStep = ms => { window.__vtNow += ms; const c = q; q = []; for (const f of c) { try { f(window.__vtNow); } catch (e) { console.log('vterr ' + e.message); } } return c.length; };
  }, save);
  const p = await ctx.newPage(); p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('file://' + page + '?nostat=1&autostart=1');
  for (let k = 0; k < 300; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { try { const G = window.__W().G; const c = document.getElementById('cont'); if (c && c.getClientRects().length && !window.__lxc) { window.__lxc = 1; setTimeout(() => c.click(), 10); } const w = document.getElementById('wgo'); if (w) w.click(); return G.mode + '|' + !!window.__zonesPretes; } catch (e) { return 'x'; } }); if (/^play\|true/.test(st) && k > 3) break; }
  await p.evaluate(() => { const W = window.__W(), T = window.__T(), G = W.G; const g = document.getElementById('guide'); if (g) g.remove(); if (G.mode !== 'play') G.mode = 'play'; if (G.onFoot && G.parked) { G.inside = false; T.finishEnter({ own: true }); } window.__drive = { fwd: 0, side: 0, brake: true }; window.__auto = () => window.__drive; if (T.P) T.P.nightStart = false; document.body.classList.add('cinema'); });
  let f = +(process.env.F0 || 0);
  for (const [n, x, z, h, hr, sec, fwd, side] of SEGS) {
    await p.evaluate(([x, z, h, hr]) => { window.__vt = 0; const W = window.__W(), G = W.G, c = G.car; W.creatorSetHour(hr); c.x = x; c.z = z; c.h = h; c.v = 0; c.jy = null; G.snapCam = true; window.__drive = { fwd: 0, side: 0, brake: true }; }, [x, z, h, hr]);
    await p.waitForTimeout(8000); // quartier construit en temps réel
    await p.evaluate(([fwd, side]) => { document.body.classList.add('cinema'); window.__vtOn(); for (let i = 0; i < 30; i++) window.__vtStep(1000 / 30); window.__drive = { fwd, side, brake: false }; for (let i = 0; i < 45; i++) window.__vtStep(1000 / 30); }, [fwd, side]);
    const N = Math.round(sec * 30);
    for (let i = 0; i < N; i++) { await p.evaluate(() => window.__vtStep(1000 / 30)); for (let r = 0; r < 3; r++) { try { await p.screenshot({ path: `${out}/f${String(f).padStart(5, '0')}.jpg`, type: 'jpeg', quality: 92, timeout: 120000 }); break; } catch (e) { console.log('retry', f); } } f++; }
    console.log('seg', n, N, await p.evaluate(() => { const c = window.__W().G.car; return [c.x | 0, c.z | 0, +c.v.toFixed(1)]; }));
  }
  await b.close(); })();
