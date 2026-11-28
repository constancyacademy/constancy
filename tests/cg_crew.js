// V310.136 · « Rejoins-moi » sur CrazyGames : SDK simulé (lien d'invitation, paramètre p), script simulé (action=crew), cadeau de l'ami à sa 1re livraison, carte « My crew », récompense de celui qui invite
// node tests/cg_crew.js http://127.0.0.1:PORT/index.html   (zip cg construit avec l'accès de test window.__CGT)
const { chromium } = require('playwright');
(async () => { const url = process.argv[2], out = process.argv[3] || '/tmp/crew_';
  const b = await chromium.launch({ args: ['--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--mute-audio'] });
  const ctx = await b.newContext({ viewport: { width: 1280, height: 720 } }); const calls = [];
  await ctx.route(/^https?:\/\/(?!127\.0\.0\.1)/, r => { const u = r.request().url();
    if (/sdk\.crazygames\.com/.test(u)) return r.fulfill({ contentType: 'application/javascript', body: `window.CrazyGames={SDK:{environment:"local",init:()=>Promise.resolve(),game:{loadingStart(){},loadingStop(){},gameplayStart(){},gameplayStop(){},happytime(){},inviteLink:o=>"https://www.crazygames.com/game/constancy?p="+o.p,getInviteParam:k=>k==="p"?"abcdef123456":null},ad:{requestAd(){},hasAdblock:()=>Promise.resolve(false)},user:{isUserAccountAvailable:false},data:{getItem(){return null},setItem(){},removeItem(){},clear(){}}}};` });
    if (/script\.google\.com/.test(u)) { calls.push(u.replace(/^.*\?/, '').slice(0, 160)); if (/action=crew/.test(u)) return r.fulfill({ contentType: 'application/json', headers: { 'access-control-allow-origin': '*' }, body: JSON.stringify({ n: 2, list: [{ p: 'Player AB12', d: 2, c: 4300 }, { p: 'Player ZZ90', d: 1, c: 1750 }] }) }); return r.fulfill({ contentType: 'text/plain', headers: { 'access-control-allow-origin': '*' }, body: 'ok' }); }
    return r.abort(); });
  await ctx.addInitScript(() => { Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }); });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message)); await p.goto(url);
  await p.waitForFunction(() => (window.__stats || []).includes('partie-lancee'), null, { timeout: 900000 });
  console.log('ARRIVÉE', await p.evaluate(() => JSON.stringify({ ref: localStorage.getItem('constancy-ref'), stat: (window.__stats || []).filter(s => /invite/.test(s)) })));
  await p.waitForFunction(() => { const G = window.__CGT().G; return !!(G.mission && G.mission.type === 'livraison'); }, null, { timeout: 240000 }).catch(() => {});
  const c0 = await p.evaluate(() => window.__CGT().P.cash);
  await p.evaluate(() => { const G = window.__CGT().G, M = G.mission; const o = G.onFoot ? G.me : G.car; o.x = M.dx + 2; o.z = M.dz + 2; G.snapCam = true; if (G.car) G.car.v = 0; });
  await p.waitForFunction(() => (window.__stats || []).includes('livraison-1'), null, { timeout: 120000 }).catch(() => console.log('pas livré'));
  await p.evaluate(() => { const X = window.__CGT(); X.P.playS = Math.max(X.P.playS || 0, 30); }); await p.waitForTimeout(6000);
  for (let k = 0; k < 30; k++) { const ok = await p.evaluate(() => (window.__stats || []).includes('bienvenue-filleul')); if (ok) break; await p.waitForTimeout(1000); }
  console.log('AMI', await p.evaluate(c0 => { const X = window.__CGT(); return JSON.stringify({ refWelcome: X.P.refWelcome, crew: X.P.badges && X.P.badges.crew, gain: X.P.cash - c0, stats: (window.__stats || []).filter(s => /filleul|invite/.test(s)) }); }, c0));
  await p.evaluate(() => { const X = window.__CGT(); X.G.mission = null; X.openMenu(); }); await p.waitForTimeout(1500);
  console.log('MENU', await p.evaluate(() => { const b = document.getElementById('shareM'); return b ? b.innerText : 'ABSENT'; }));
  const c1 = await p.evaluate(() => window.__CGT().P.cash); await p.evaluate(() => document.getElementById('shareM').click()); await p.waitForTimeout(4000); await p.screenshot({ path: out + 'carte.png' });
  console.log('CARTE', await p.evaluate(c1 => { const X = window.__CGT(); return JSON.stringify({ lien: (document.getElementById('crewLink') || {}).value, liste: (document.getElementById('crewList') || {}).innerText, gain: X.P.cash - c1, paid: X.P.filleulsPaid, crew: X.P.badges && X.P.badges.crew, texte: document.querySelector('#screen .panel').innerText.replace(/\s+/g, ' ').slice(0, 220) }); }, c1));
  console.log('APPELS SCRIPT', JSON.stringify(calls.filter(c => /ref=|crew/.test(c)).slice(0, 4)));
  console.log('MANQUES', JSON.stringify(await p.evaluate(() => window.__i18nMiss ? window.__i18nMiss().filter(k => /[éèàùç]|\b(le|la|ton|toi|tes|pour|ami)\b/i.test(k)).slice(0, 10) : 'x')));
  console.log('ERR', errs.slice(0, 3).join(' | ') || 'none'); await b.close(); })();
