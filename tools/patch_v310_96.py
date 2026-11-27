# V310.96 · DATA · chiffres vrais des joueurs des plateformes (tâche 2 de la file du 27/11 8h07, données fausses D1, D2, D4, D5)
# Usage, depuis la racine du dépôt : python3 tools/patch_v310_96.py  (refuse si un texte de départ a changé · s'applique avant ou après V310.94 et V310.95)
# 1. minutes = temps ACTIF seulement (page visible et un toucher, un clic ou une touche dans les 60 dernières secondes)
# 2. plus aucun envoi après 30 min sans aucun toucher (onglet oublié), un seul envoi au retour du joueur
# 3. &jj= jours réels joués, &mi= missions faites, &t=1 si le SDK dit aperçu ou test (CrazyGames environment ≠ crazygames, Playgama mock, qa_tool ou playgama_sandbox)
import os, re
R = os.getcwd(); p = os.path.join(R, "index.html"); s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: raise SystemExit("REFUS : texte de départ trouvé %d fois : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep('const PL = { rank: 0, step: "", t: 0, iv: 0 },',
    'const PL = { rank: 0, step: "", t: 0, iv: 0, act: Date.now(), actMs: 0, idle: false },')
rep('function plId() {',
    '/* V310.96 (expert, données fausses D2 : une ligne CrazyGames à 1 071 min sur « Accueil », onglet oublié) : on ne compte que le temps actif, et plus rien ne part après 30 min sans toucher */\n'
    'if (PORTAL) { const plAct = () => { const w = PL.idle; PL.act = Date.now(); if (w) { PL.idle = false; PL.t = Date.now(); plSend(); } }; ["pointerdown", "touchstart", "keydown", "wheel"].forEach(ev => addEventListener(ev, plAct, { passive: true, capture: true })); setInterval(() => { if (!document.hidden && Date.now() - PL.act < 60000) PL.actMs += 5000; }, 5000); }\n'
    'function plTest() { try { if (PORTAL === "cg" && PSDK.cg && PSDK.cg.environment && PSDK.cg.environment !== "crazygames") return 1; if (PORTAL === "pg" && PSDK.pg && PSDK.pg.platform && /^(mock|qa_tool|playgama_sandbox)$/.test(String(PSDK.pg.platform.id))) return 1; } catch (e) {} return 0; }\n'
    'function plId() {')
rep('if (PL.t) min += Math.min(10, (now - PL.t) / 60000); PL.t = now;',
    'if (PL.t) min += Math.min(10, PL.actMs / 60000); PL.actMs = 0; PL.t = now; /* V310.96 : temps actif seulement */')
rep('+ "&k=" + (localStorage.getItem("cst-pl-k") ? 1 : 0);',
    '+ "&k=" + (localStorage.getItem("cst-pl-k") ? 1 : 0) + "&jj=" + Math.max(1, (P && P.playDates && P.playDates.length) || 1) + "&mi=" + (P && P.counts ? Object.values(P.counts).reduce((a, v) => a + (+v || 0), 0) : 0) + (plTest() ? "&t=1" : "");')
rep('if (!PL.iv) { PL.iv = setInterval(() => plSend(), 180000);',
    'if (!PL.iv) { PL.iv = setInterval(() => { if (Date.now() - PL.act > 1800000) { PL.idle = true; return; } plSend(); }, 180000);')
open(p, "w", encoding="utf-8").write(s)
w = os.path.join(R, "sw.js"); ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611271315';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
