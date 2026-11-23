// R4 : mesure en 4G bridée (méthode de l'expert du 21/11 : 10 Mbit/s, 70 ms) du chemin direct depuis un réel (?s=ig) : écran « Touchez pour jouer », octets, modèles arrivés, puis rêve
// Usage : node g4.js http://localhost:PORT/page.html
const { chromium } = require('playwright');
(async () => { const url = process.argv[2]; const b = await chromium.launch({ args: ['--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 1, userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 350.0.0.0' });
  await ctx.route(/^https?:\/\/(?!localhost)/, r => r.abort()); await ctx.addInitScript(() => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); });
  const p = await ctx.newPage(); const cdp = await ctx.newCDPSession(p); await cdp.send('Network.enable'); await cdp.send('Network.emulateNetworkConditions', { offline: false, latency: 70, downloadThroughput: 10e6 / 8, uploadThroughput: 4e6 / 8 });
  let bytes = 0, files = 0; const urls = {}, fin = []; cdp.on('Network.requestWillBeSent', e => { urls[e.requestId] = e.request.url.split('/').pop().slice(0, 40); }); cdp.on('Network.loadingFinished', e => { bytes += e.encodedDataLength; files++; fin.push([((Date.now() - t0) / 1000).toFixed(1), urls[e.requestId], Math.round(e.encodedDataLength / 1024)]); });
  let t0 = Date.now(); const T = () => ((Date.now() - t0) / 1000).toFixed(1) + 's', MB = () => (bytes / 1048576).toFixed(1) + ' Mo';
  await p.goto(url + (url.includes('?') ? '&' : '?') + 'nostat=1&s=ig', { waitUntil: 'commit' });
  await p.waitForFunction(() => { const b = document.querySelector('.boot'); return b && b.classList.contains('ready'); }, null, { timeout: 900000, polling: 200 });
  const m = await p.evaluate(() => { const M = window.__W && window.__W().MODELS; return M ? Object.keys(M).length : -1; });
  const big = fin.filter(f => f[2] > 300).map(f => f[0] + 's ' + f[1] + ' ' + f[2] + 'k'); console.log('GROS FICHIERS AVANT PRET', big.join(' | ')); console.log('DERNIERS', fin.slice(-6).map(f => f[0] + 's ' + f[1]).join(' | ')); console.log('PRET', T(), MB(), files + ' fichiers', 'modèles', m, (await p.evaluate(() => (document.querySelector('.bgT') || {}).textContent)));
  const tt = Date.now(); await p.evaluate(() => { const g = document.getElementById('bootGo'); if (g) g.click(); });
  await p.waitForFunction(() => window.__W && window.__W().DREAM && window.__W().DREAM.on, null, { timeout: 900000, polling: 200 });
  console.log('REVE', ((Date.now() - tt) / 1000).toFixed(1) + 's après le toucher', 'total', T(), MB(), 'modèles', await p.evaluate(() => Object.keys(window.__W().MODELS || {}).length), 'stats', await p.evaluate(() => (window.__stats || []).filter(s => /debut|splash/.test(s)).join(' ')));
  await b.close(); })().catch(e => { console.log('ERREUR', e.message.slice(0, 300)); process.exit(1); });
