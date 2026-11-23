// Flash blanc sur ordinateur (Thomas 23/11 16h23) : capture continue (screencast) du rêve au miroir, sur ordinateur, et relève toute image presque blanche
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const page = path.resolve(process.argv[2]), out = process.argv[3] || '/tmp/pc/fl/'; fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch({ args: ['--allow-file-access-from-files', '--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 640, height: 400 }, deviceScaleFactor: 1 });
  await ctx.route(/^https?:/, r => r.abort()); await ctx.addInitScript(() => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 200)));
  await p.goto('file://' + page + '?nostat=1&autostart=1'); await p.waitForSelector('#quick', { timeout: 900000 }); console.log('accueil');
  const cdp = await ctx.newCDPSession(p); let n = 0; const t0 = Date.now(); const lab = { v: 'titre' };
  cdp.on('Page.screencastFrame', async f => { n++; fs.writeFileSync(out + String(n).padStart(5, '0') + '_' + lab.v + '_' + (Date.now() - t0) + '.jpg', Buffer.from(f.data, 'base64')); try { await cdp.send('Page.screencastFrameAck', { sessionId: f.sessionId }); } catch (e) {} });
  await cdp.send('Page.startScreencast', { format: 'jpeg', quality: 50, everyNthFrame: 1 });
  await p.evaluate(() => setTimeout(() => document.getElementById('quick').click(), 10));
  for (let k = 0; k < 140; k++) { await p.waitForTimeout(1000); const st = await p.evaluate(() => { const W = window.__W(); return { dream: !!W.DREAM.on, ok: !!(document.getElementById('ok') && document.getElementById('ok').getClientRects().length), em: !!document.getElementById('em'), mode: W.G.mode }; }); lab.v = st.dream ? 'reve' : st.ok ? 'miroir' : st.em ? 'mur' : st.mode; if (st.ok && !lab.okT) lab.okT = k; if (lab.okT && k - lab.okT > 12) break; }
  await cdp.send('Page.stopScreencast'); console.log('images', n, 'ERR', errs.slice(0, 3).join(' | ') || 'none'); await b.close(); })().catch(e => { console.log('ERREUR', e.message.slice(0, 300)); process.exit(1); });
