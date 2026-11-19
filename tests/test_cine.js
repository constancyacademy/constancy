// prologue + interview + talkie : captures aux bons instants (temps du jeu, pas temps réel)
const { chromium } = require('playwright'); const fs = require('fs');
(async () => { const [,, page, pre] = process.argv;
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const p = await (await b.newContext({ viewport: { width: 540, height: 960 } })).newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + require('path').resolve(page) + '?nostat=1'); await p.waitForSelector('#quick', { timeout: 400000 });
  await p.click('#quick', { force: true, noWaitAfter: true, timeout: 600000 }); await p.waitForSelector('#ok, .choice', { timeout: 600000 }); if (await p.$('#ok')) { await p.waitForTimeout(400); await p.evaluate(() => document.getElementById('ok').click()); }
  await p.waitForTimeout(4000);
  await p.evaluate(() => { const W = window.__W(); if (W.P) { W.P.storyI = 99; W.P.dayT = 300; } W.G.mission = null; window.__outHome = 1; W.G.inside = false; W.G.intro = null; W.G.afterCar = null; document.querySelectorAll('#screen').forEach(e => e.classList.add('hidden')); });
  await p.waitForTimeout(3000);
  // prologue au pied d'un immeuble du centre
  await p.evaluate(() => { const W = window.__W(); W.G.onFoot = true; W.G.me.x = 20; W.G.me.z = 40; W.G.me.h = 0; window.__prologue(); });
  const shots = [2.0, 4.0, 6.5, 9.0, 12.5, 16.5, 20.0, 23.5, 26.0]; let k = 0; const t0 = Date.now();
  while (k < shots.length && Date.now() - t0 < 900000) { const t = await p.evaluate(() => { try { const C = window.__F().CINE; return C.on ? C.t : 99; } catch (e) { return -1; } }); if (t >= shots[k]) { await p.screenshot({ path: `${pre}pro_${String(k).padStart(2, '0')}_${t.toFixed(1)}.png` }); console.log('shot', k, t.toFixed(2)); k++; } else await p.waitForTimeout(150); if (t === 99) break; }
  await p.waitForTimeout(3000); await p.evaluate(() => window.__talkie(2)); await p.waitForTimeout(1500); await p.screenshot({ path: pre + 'talkie.png' }); console.log('talkie');
  await p.waitForTimeout(6000); await p.evaluate(() => window.__interview()); for (const want of [1.0, 2.5, 4.0]) { while ((await p.evaluate(() => window.__F().ITV.on ? window.__F().ITV.t : 99)) < want) await p.waitForTimeout(120); await p.screenshot({ path: `${pre}itv_${want}.png` }); console.log('itv', want); }
  console.log(await p.evaluate(() => { const W = window.__W(), out = []; W.RDX.list.forEach(Q => { if (!Q.deck) return; let st = -1; for (let i = 0; i <= Q.P.length; i++) { const d = i < Q.P.length && Q.deck[i]; if (d && st < 0) st = i; if (!d && st >= 0) { const a = Q.P[st], e = Q.P[i - 1]; out.push(`PONT ${Q.D.id} ${Q.D.name} : (${Math.round(a[0])},${Math.round(a[1])}) → (${Math.round(e[0])},${Math.round(e[1])}) ${i - st} pts`); st = -1; } } }); return out.join('\n'); }));
  console.log('errs', JSON.stringify(errs.slice(0, 8))); await b.close(); })();
