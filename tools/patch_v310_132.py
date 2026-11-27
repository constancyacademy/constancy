# V310.132 · PLAYGAMA (correctif de l'expert, claude/constancy-correctif-playgama-pub-27-11.txt) · porte pg seulement
# 1. « ▶ Watch an ad · +$500 » dans le menu Pause, à côté de « My collection », toujours là hors mission (pas de délai, pas de plafond par jour sur pg)
# 2. petit bouton en jeu : plus aucun délai dans l'outil de test Playgama (mock, qa_tool, playgama_sandbox), 5 min sinon
# 3. le jeu est en pause pendant la pub ; « Close (No Reward) » = aucune récompense, le jeu reprend, le son revient
# 4. notification « Défi du jour » découpée en morceaux traduisibles (le texte reste identique en français)
# Usage, depuis la racine du dépôt : python3 tools/patch_v310_132.py
import os, re
R = os.getcwd(); p = os.path.join(R, "index.html"); s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: raise SystemExit("REFUS : texte de départ trouvé %d fois : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
# 1. plafond de 5 pubs par jour : plus sur pg
rep('function adAvailable() { return (ADS_ON || PORTAL === "pg") && !!adSdk() && !G.mission && (!P.adD || P.adD.d !== P.day || P.adD.n < 5); }',
    'function adAvailable() { return (ADS_ON || PORTAL === "pg") && !!adSdk() && !G.mission && (PORTAL === "pg" || !P.adD || P.adD.d !== P.day || P.adD.n < 5); } /* V310.132 : pas de plafond par jour sur Playgama (pub toujours au choix du joueur) */')
# 2. petit bouton en jeu : pas de délai dans l'outil de test Playgama
rep('adAvailable() && Date.now() - (pgAdBtn.t || 0) > 300000 && !pgAdBtn.busy;',
    'adAvailable() && Date.now() - (pgAdBtn.t || 0) > (plTest() ? 0 : 300000) && !pgAdBtn.busy; /* V310.132 : aucun délai dans l\'outil de test Playgama */')
rep('stat("pub-pg-clic"); adRewarded(); });',
    'stat("pub-pg-clic"); adPause(); adRewarded(); });')
# 3. pause pendant la pub, reprise du jeu à la fin (récompense ou pas)
rep('function adRewarded() { const k = adSdk(); if (!k || G.mission) { pgAdBtn.busy = 0; return; } const pgM = PORTAL === "pg"; const ok = () => { if (ok.d) return; ok.d = 1; pgAdBtn.busy = 0; pgAdBtn.t = Date.now(); P.adD = P.adD && P.adD.d === P.day ? P.adD : { d: P.day, n: 0 }; P.adD.n++; if (pgM) { addCash(500, true);',
    '/* V310.132 : le jeu s\'arrête pendant la pub (mode menu, sans panneau) et repart à la fin */ function adPause() { if (PORTAL !== "pg") return; try { hideScreen(); if (G.mode === "play" || G.mode === "menu") { setMode("menu"); adRewarded.pz = 1; } } catch (e) {} }\n'
    'function adUnpause() { if (!adRewarded.pz) return; adRewarded.pz = 0; try { if (G.mode === "menu" && screen.classList.contains("hidden")) resume(); const c = SND.ctx; if (c && c.state === "suspended" && SND.on !== false) c.resume(); } catch (e) {} }\n'
    'function adRewarded() { const k = adSdk(); if (!k || G.mission) { pgAdBtn.busy = 0; adUnpause(); return; } const pgM = PORTAL === "pg"; const ok = () => { if (ok.d) return; ok.d = 1; pgAdBtn.busy = 0; pgAdBtn.t = Date.now(); P.adD = P.adD && P.adD.d === P.day ? P.adD : { d: P.day, n: 0 }; P.adD.n++; if (pgM) { adUnpause(); addCash(500, true);')
rep('ko = () => { if (ko.d || ok.d) return; ko.d = 1; pgAdBtn.busy = 0; pgAdBtn.t = Date.now() - 240000; if (!pgM) openShop(null, "packs"); };',
    'ko = () => { if (ko.d || ok.d) return; ko.d = 1; pgAdBtn.busy = 0; pgAdBtn.t = Date.now() - 240000; if (pgM) { adUnpause(); stat("pub-pg-sans-recompense"); help("Ad closed · no reward this time.", 3); return; } openShop(null, "packs"); };')
# 1 bis. bouton du menu Pause, à côté de « Ma collection »
rep('<button class="pm-t pk" id="collM" type="button">${pmIcon("perso")}<span>Ma collection</span></button>',
    '<button class="pm-t pk" id="collM" type="button">${pmIcon("perso")}<span>Ma collection</span></button>\n'
    '      ${PORTAL === "pg" && !CREATOR && adAvailable() ? `<button class="pm-t pk" id="pgAdM" type="button" style="background:rgba(255,45,149,.92);color:#fff"><span>▶ Watch an ad · +$500</span></button>` : ""}')
rep('on("collM", () => openCollection()); on("shopM", () => openShop());',
    'on("collM", () => openCollection()); on("shopM", () => openShop());\n'
    '  on("pgAdM", () => { if (pgAdBtn.busy) return; pgAdBtn.busy = 1; stat("pub-pg-clic-menu"); adPause(); adRewarded(); }); /* V310.132 */')
# 4. Défi du jour : morceaux traduisibles
rep('notify("info", `<b>Défi du jour · ${D.t}.</b> ${D.d} Il change chaque jour. 7 jours d\'affilée = gros bonus.`, 8);',
    'notify("info", `<b>Défi du jour · ${D.t}.</b> <span>${D.d}</span> <span>Il change chaque jour. 7 jours d\'affilée = gros bonus.</span>`, 8); /* V310.132 : morceaux séparés pour la traduction */')
open(p, "w", encoding="utf-8").write(s)
w = os.path.join(R, "sw.js"); ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611280045';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
