// profil de performance : 390x844 (téléphone), partie lancée, 3 lieux (ville, parc, périphérie sud), temps par fonction et par image
const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const p = await (await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true })).newPage();
  p.on('pageerror', e => console.log('PAGEERR', e.message.slice(0, 200)));
  await p.goto('file://' + path.resolve(process.argv[2]) + '?nostat=1&noprologue=1&prof=1'); await p.evaluate(() => { try { sessionStorage.setItem('cst-relance', '1'); } catch (e) {} });
  await p.waitForSelector('#quick', { timeout: 900000 }); await p.click('#quick', { force: true, noWaitAfter: true, timeout: 600000 }); await p.waitForSelector('#ok, .choice', { timeout: 600000 }); if (await p.$('#ok')) await p.evaluate(() => document.getElementById('ok').click());
  await p.waitForSelector('.choice', { timeout: 600000 }); await p.click('.choice', { force: true, noWaitAfter: true, timeout: 600000 }); await p.waitForTimeout(4000);
  await p.evaluate(() => { const W = window.__W(); if (W.P) W.P.storyI = 99; W.G.mission = null; window.__outHome = 1; W.G.inside = false; W.G.intro = null; W.G.afterCar = null; });
  for (const [nm, x, z] of [['ville', 0, 60], ['parc', 130, -2690], ['sud', 200, 900]]) {
    await p.evaluate(([x, z]) => { const W = window.__W(); W.G.me.x = x; W.G.me.z = z; W.G.me._lx = x; W.G.me._lz = z; W.G.onFoot = true; for (const k in window.__PROF) delete window.__PROF[k]; window.__PROFR.t = 0; window.__PROFR.n = 0; }, [x, z]);
    await p.waitForTimeout(25000);
    const r = await p.evaluate(() => { const P = window.__PROF, R = window.__PROFR, n = Math.max(1, R.n), ri = window.__X ? null : null; const rows = Object.entries(P).map(([k, v]) => [k, v.t / n]).sort((a, b) => b[1] - a[1]).slice(0, 14); const inf = window.__dbg ? window.__dbg() : {}; return { frames: R.n, render: (R.t / n).toFixed(1), calls: inf.calls, tri: inf.triangles, top: rows.map(([k, v]) => k + ' ' + v.toFixed(2)).join(' | ') }; });
    console.log('LIEU', nm, JSON.stringify(r)); }
  await b.close(); })();
