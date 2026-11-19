// node cap.js out_dir shots.json  (frame-stepped capture at 30 fps)
const { chromium } = require('playwright'); const fs = require('fs');
(async () => { const [,, out, sf] = process.argv; const S = JSON.parse(fs.readFileSync(sf, 'utf8')); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: S.w || 1080, height: S.h || 1920 } }); const p = await ctx.newPage();
  const VD = process.env.VD; const MAP = {}; for (const l of fs.readFileSync(VD + '/map.txt', 'utf8').trim().split('\n')) { const [u, f] = l.split(' '); MAP[u] = VD + '/' + f.replace('vendor/', ''); } MAP['https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js'] = VD + '/three.min.js';
  await ctx.route(/^https?:/, r => { const u = r.request().url(); if (MAP[u]) return r.fulfill({ path: MAP[u], contentType: 'application/javascript' }); return r.abort(); });
  await p.addInitScript(() => { const rP = performance.now.bind(performance), rD = Date.now, rRAF = window.requestAnimationFrame.bind(window); let fz = false, vt = 0, q = []; const d0 = rD(), p0 = rP();
    performance.now = () => fz ? vt : rP(); Date.now = () => fz ? Math.round(d0 + (vt - p0)) : rD();
    window.requestAnimationFrame = cb => { if (!fz) return rRAF(cb); q.push(cb); return q.length; };
    window.__freeze = () => { vt = rP(); fz = true; }; window.__step = ms => { vt += ms; const c = q; q = []; for (const f of c) { try { f(vt); } catch (e) { console.log('STEPERR ' + e.message); } } return c.length; }; });
  p.on('pageerror', e => console.log('PAGEERR', e.message)); const t0 = Date.now();
  await p.goto(S.url, { timeout: 300000 }); await p.waitForSelector('#quick', { timeout: 400000 }); console.log('quick', (Date.now() - t0) / 1000);
  await p.click('#quick', { force: true, noWaitAfter: true, timeout: 600000 }); await p.waitForSelector('#ok, .choice', { timeout: 600000 }); if (await p.$('#ok')) { await p.waitForTimeout(400); await p.evaluate(() => document.getElementById('ok').click()); } await p.waitForSelector('.choice', { timeout: 600000 }); await p.click('.choice', { force: true, noWaitAfter: true, timeout: 600000 }); await p.waitForTimeout(2500); if (await p.$('#gSkip')) await p.click('#gSkip', { force: true, noWaitAfter: true, timeout: 600000 }); await p.waitForTimeout(500);
  await p.evaluate(() => { const W = window.__W(); if (W.P) { W.P.storyI = 99; } W.G.mission = null; window.__outHome = 1; W.G.inside = false; W.G.intro = null; W.G.afterCar = null; });
  console.log('started', await p.evaluate(() => { const W = window.__W(); return { s: !!(W.P && W.G.started), me: [W.G.me.x, W.G.me.z, W.G.me.h], car: W.G.car && [W.G.car.x, W.G.car.z, W.G.car.h] }; }));
  await p.waitForTimeout(3000); await p.addStyleTag({ content: 'body *:not(#game){visibility:hidden!important} #game{visibility:visible!important}' });
  console.log('load', (Date.now() - t0) / 1000);
  for (const v of S.shots) { await p.evaluate(v => { const W = window.__W(); window.__outHome = 1; W.G.inside = false; W.G.intro = null; W.G.afterCar = null; W.G.mission = null; W.G.started = true; if (W.P) { W.P.day = 2; W.P.nightStart = 0; W.P.dayT = v.dayT || 600; } window.__wx = 0; W.WX.rain = 0;
      if (v.js) eval(v.js); window.__T0 = null; window.__camK = eval(v.camjs); W.camera.far = Math.max(W.camera.far, v.far || 0); }, v);
    await p.waitForTimeout(v.wait || 5000); await p.evaluate(() => window.__freeze()); await p.evaluate(() => { window.__T0 = performance.now(); });
    const n = v.n || 90; const ts = Date.now();
    for (let i = 0; i < (v.pre || 3); i++) await p.evaluate(() => window.__step(1000 / 30));
    for (let i = 0; i < n; i++) { await p.evaluate(() => window.__step(1000 / 30)); await p.screenshot({ path: `${out}/${v.name}_${String(i).padStart(3, '0')}.png`, timeout: 240000 }); if (i == 0 || i % 15 == 0) console.log(v.name, i, (Date.now() - ts) / 1000); if (v.one) break; }
    await p.evaluate(() => { location.reload = null; }); }
  await b.close(); })();
