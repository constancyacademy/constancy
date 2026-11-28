// V310.133 · CrazyGames : entrée directe, Mo et secondes jusqu'à l'entrée en jeu (gameplayStart), suite téléchargée en jeu, zones lointaines construites ensuite, 1re livraison en anglais, 0 erreur
// node tests/cg_depart.js http://127.0.0.1:PORT/index.html sortie_   (zip cg construit avec l'accès de test window.__CGT)
const { chromium } = require('playwright');
(async () => { const url = process.argv[2], out = process.argv[3] || '/tmp/cgd_';
  const b = await chromium.launch({ args: ['--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 1280, height: 720 } }); await ctx.route(/^https?:\/\/(?!127\.0\.0\.1)/, r => r.abort());
  await ctx.addInitScript(() => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
  const cdp = await ctx.newCDPSession(p); await cdp.send('Network.enable'); let tot = 0; cdp.on('Network.loadingFinished', e => { tot += e.encodedDataLength; });
  const t0 = Date.now(); await p.goto(url + '?nostat=1');
  await p.waitForFunction(() => (window.__stats || []).includes('partie-lancee'), null, { timeout: 900000 }); const tPlay = (Date.now() - t0) / 1000, moPlay = tot / 1e6;
  console.log('EN JEU', tPlay.toFixed(1) + ' s', moPlay.toFixed(2) + ' Mo (brut, sans compression)', 'titre PLAY :', await p.evaluate(() => !!document.getElementById('pkTitle')));
  await p.waitForFunction(() => { const G = window.__CGT().G; return !!(G.mission && G.mission.type === 'livraison'); }, null, { timeout: 240000 }).catch(() => {}); console.log('MISSION À', ((Date.now() - t0) / 1000 - tPlay).toFixed(1), 's après l\'entrée en jeu');
  const m = await p.evaluate(() => { const G = window.__CGT().G; return G.mission ? { t: G.mission.type, x: G.mission.dx, z: G.mission.dz } : null; }); console.log('MISSION', JSON.stringify(m));
  if (m) { await p.evaluate(m => { const G = window.__CGT().G; const o = G.onFoot ? G.me : G.car; o.x = m.x + 2; o.z = m.z + 2; G.snapCam = true; if (G.car) G.car.v = 0; }, m); for (let k = 0; k < 40; k++) { await p.waitForTimeout(1000); const ok = await p.evaluate(() => (window.__stats || []).some(s => /^livraison-1$/.test(s))); if (ok) break; } }
  await p.waitForTimeout(1500); await p.screenshot({ path: out + 'livre.png' });
  console.log('LIVRÉ', await p.evaluate(() => JSON.stringify({ livraison: (window.__stats || []).filter(s => /livraison-1/.test(s)), help: (document.getElementById('help') || {}).innerText })));
  await p.waitForFunction(() => window.__cgSuite != null, null, { timeout: 600000 }); console.log('SUITE TÉLÉCHARGÉE en', await p.evaluate(() => window.__cgSuite), 'ms ·', ((tot / 1e6) - moPlay).toFixed(2), 'Mo de plus');
  await p.waitForFunction(() => window.__zonesPretes === true, null, { timeout: 600000 }).catch(() => {}); console.log('ZONES', await p.evaluate(() => { const X = window.__CGT(); return JSON.stringify({ dalles: window.__cgTiles, look: X.P && X.P.look && X.P.look.gender, obj: X.P && X.P.goal && X.P.goal.type, pretes: !!window.__zonesPretes, reste: X.DEFER.q.map(i => i[0]), modeles: X.MODELS_N, temps: X.DEFER.t.slice(-6) }); }));
  await p.screenshot({ path: out + 'jeu.png' });
  console.log('FRANÇAIS RESTANT', JSON.stringify(await p.evaluate(() => window.__i18nMiss ? window.__i18nMiss().filter(k => /[éèàùçêô]|\b(le|la|les|ton|ta|tes|est|une|des|pour)\b/i.test(k)).slice(0, 20) : 'x')));
  console.log('ERR', errs.length ? errs.slice(0, 3).join(' | ') : 'none'); await b.close(); })();
