// Mémoire brassée du chargement jusqu'à l'accueil + 8 s (HeapProfiler, objets ramassés compris) · node churn.js page.html
const { chromium } = require('playwright'); const path = require('path');
(async () => { const page = path.resolve(process.argv[2]);
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio', '--enable-precise-memory-info'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, hasTouch: true, isMobile: true, userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 350.0.0.0' });
  await ctx.route(/^https?:/, r => r.abort()); await ctx.addInitScript(() => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); });
  const p = await ctx.newPage(); const cdp = await ctx.newCDPSession(p); await cdp.send('HeapProfiler.enable');
  await cdp.send('HeapProfiler.startSampling', { samplingInterval: 32768, includeObjectsCollectedByMajorGC: true, includeObjectsCollectedByMinorGC: true });
  await p.goto('file://' + page + '?nostat=1&s=ig&autostart=1'); await p.waitForSelector('#quick', { timeout: 900000 }); await p.waitForTimeout(8000);
  const { profile } = await cdp.send('HeapProfiler.stopSampling'); let tot = 0; const byFn = {}; const walk = (n, stack) => { const self = n.selfSize || 0; tot += self; const fn = n.callFrame.functionName || '(anon)'; byFn[fn] = (byFn[fn] || 0) + self; (n.children || []).forEach(c => walk(c)); }; walk(profile.head);
  const top = Object.entries(byFn).sort((a, b) => b[1] - a[1]).slice(0, 10).map(([k, v]) => k + ' ' + Math.round(v / 1048576) + ' Mo');
  let eq = null; try { eq = await p.evaluate(() => { const T = window.__T && window.__T(); if (!T || !T.bioWeightsN) return null; let bad = 0, n = 0; for (let i = 0; i < 4000; i++) { const x = -2600 + Math.random() * 4200, z = -3800 + Math.random() * 5700, A = T.bioWeights(x, z), k = T.bioWeightsN(x, z); n++; if (A.length !== k) { bad++; continue; } for (let q = 0; q < k; q++) if (A[q][0] !== T.BWI[q] || Math.abs(A[q][1] - T.BWW[q]) > 1e-12) { bad++; break; } } return { n, bad, bio: T.BIO.length }; }); } catch (e) { eq = e.message.slice(0, 80); }
  console.log('BRASSÉ', Math.round(tot / 1048576), 'Mo'); console.log('TOP', top.join(' · ')); console.log('ÉGALITÉ', JSON.stringify(eq)); await b.close(); })().catch(e => { console.log('ERREUR', e.message.slice(0, 300)); process.exit(1); });
