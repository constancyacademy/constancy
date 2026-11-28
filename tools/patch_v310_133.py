# V310.133 · CORRECTIFS DE LA BUSINESS DU 28/11 (claude/constancy-correctif-playgama-pub-27-11.txt, 9h50 à 10h00)
# 1. CRAZYGAMES : plus d'écran « ▶ PLAY » (retour à l'entrée directe de la V310.117) · moins de Mo avant le 1er gameplayStart :
#    - les modèles des zones lointaines (Mont, parc, lieux de la campagne, animaux sauvages, ferme, arbres de campagne) ne se téléchargent qu'une fois le joueur en jeu,
#      et ces 3 zones ne se construisent qu'après (elles sont loin du départ) · les musiques et bruitages secondaires aussi
#    - dinosaures jamais téléchargés au départ sur une plateforme (avant : téléchargés si le navigateur est piloté, comme un outil de test)
# 2. PLAYGAMA : « jeu prêt » (game_ready) envoyé juste après bridge.initialize(), dans un try à part, avant tout rendu 3D
# 3. Textes : traduction phrase par phrase quand une phrase complète manque (« Livre ton premier kebab. Le GPS est réglé… »)
# Usage, depuis la racine du dépôt : python3 tools/patch_v310_133.py
import os, re
R = os.getcwd(); p = os.path.join(R, "index.html"); s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: raise SystemExit("REFUS : texte de départ trouvé %d fois : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
# 1a. plus d'écran PLAY sur cg
rep('const PKH = ((PORTAL === "pk" || PORTAL === "cg") && !CREATOR)', 'const PKH = (PORTAL === "pk" && !CREATOR) /* V310.133 : plus sur CrazyGames (leur outil compte tout jusqu\'au début du jeu, toucher compris) */')
# 1b. dinosaures paresseux sur toutes les plateformes
rep('const lazyD = !navigator.webdriver', 'const lazyD = (!!PORTAL || !navigator.webdriver) /* V310.133 */')
# 1c. modèles des zones lointaines après l'entrée en jeu (cg)
rep('LATEL.keys = keys.filter(k => LATE_M.test(k)); keys = keys.filter(k => !LATE_M.test(k));',
    'LATEL.keys = keys.filter(k => LATE_M.test(k)); keys = keys.filter(k => !LATE_M.test(k));\n'
    '  if (CGL.on) { CGL.keys = keys.filter(k => CG_LATER.test(k)); keys = keys.filter(k => !CG_LATER.test(k)); CGL.hold = true; } /* V310.133 */')
rep('const HEAVY_M = ', '/* V310.133 · CrazyGames : modèles des zones loin du départ (Mont, parc, lieux de la campagne, faune sauvage, ferme), téléchargés une fois en jeu · ces zones se construisent ensuite */\n'
    'const CG_LATER = /^(w_\\w+|croc|dino_sleep|ptero3|brachio3|bungalow3|lakehouse3|cabin3|temple3|greenhouse3|lighthouse3|diner3|lookout3|cowq|combine3|horseq|goat3|horse3|cow3|tree_pine3|tree_maple3|tree_trop3|c_tree_\\w+)$/, CG_SND_LATER = /^(theme|siren|waves|gull|gymamb|door|weight|cheer|splash)$/, CGL = { on: PORTAL === "cg" && !CREATOR && !/[?&]cgall=1/.test(location.search), keys: [], hold: false, p: null, zones: ["mont", "parc", "lieux"] };\n'
    'function cgLater() { if (!CGL.on || CGL.p || G.mode !== "play") return; CGL.t0 = performance.now(); try { stat("cg-suite-debut"); } catch (e) {}\n'
    '  try { Object.entries(SND_FILES).filter(([k]) => CG_SND_LATER.test(k)).forEach(([k, u]) => fetch(u).then(r => r.ok ? r.arrayBuffer() : null).then(b => { if (b) { SNDRAW[k] = b; if (SND.ctx) decodeSnd(k); } }).catch(() => {})); } catch (e) {}\n'
    '  CGL.p = (MODELS_P || Promise.resolve()).then(() => modelWorkers(new THREE.GLTFLoader(), CGL.keys, 2, TOUCH_DEV() ? 150 : 20)).catch(() => {}).then(() => { CGL.hold = false; window.__cgSuite = Math.round(performance.now() - CGL.t0); try { stat("cg-suite-prete"); } catch (e) {} try { runDeferred("all", 250); } catch (e) {} }); }\n'
    'if (PORTAL === "cg") setInterval(() => { try { cgLater(); } catch (e) {} }, 1000);\n'
    'const HEAVY_M = ')
rep('const pick = () => { const i = DEFER.q.findIndex(it => ', 'const pick = () => { const i = DEFER.q.findIndex(it => !(CGL.hold && CGL.zones.includes(it[0])) && ')
rep('function loadLateModels() { if (LATEL.p || !THREE.GLTFLoader) return LATEL.p || Promise.resolve();',
    'function loadLateModels() { if (LATEL.p || !THREE.GLTFLoader) return LATEL.p || Promise.resolve(); if (CGL.on && !CGL.p) { setTimeout(loadLateModels, 3000); return Promise.resolve(); } /* V310.133 : sur CrazyGames, après l\'entrée en jeu */')
rep('const snds = Object.entries(SND_FILES).filter(([k]) => k !== "intro" && !(direct && k === "theme"))',
    'const snds = Object.entries(SND_FILES).filter(([k]) => k !== "intro" && !(direct && k === "theme") && !(CGL.on && CG_SND_LATER.test(k)))')
rep('if (direct) setTimeout(() => sndGet(["theme", SND_FILES.theme]), 9000);', 'if (direct && !CGL.on) setTimeout(() => sndGet(["theme", SND_FILES.theme]), 9000);')
# 2. Playgama : jeu prêt dès l'initialisation
rep('window.bridge.initialize().then(() => { PSDK.pg = window.bridge; window.__pgBridge = (window.bridge.version || "?");',
    'window.bridge.initialize().then(() => { PSDK.pg = window.bridge; window.__pgBridge = (window.bridge.version || "?"); try { if (!window.__pgReady) { window.bridge.platform.sendMessage((window.bridge.PLATFORM_MESSAGE && window.bridge.PLATFORM_MESSAGE.GAME_READY) || "game_ready"); window.__pgReady = Date.now(); window.__pgReadyT = Math.round(performance.now()); } } catch (e) {} /* V310.133 (BUSINESS 28/11 9h50 : « This archive never reported that the game was ready to play ») : le signal part tout de suite, avant WebGL et les modèles, même si le rendu 3D échoue dans leur test automatique */')
# 3. traduction phrase par phrase
rep('if (e != null) { let i = 0; const out = e.replace(/#/g, () => (nums[i++] != null ? nums[i - 1] : "#")); r = t.replace(k, out); } else if (I18N.miss.size < 3000) I18N.miss.add(key); }',
    'if (e != null) { let i = 0; const out = e.replace(/#/g, () => (nums[i++] != null ? nums[i - 1] : "#")); r = t.replace(k, out); } else { const ps = k.split(/(?<=[.!?:…])\\s+/); let hit = 0; if (ps.length > 1) { const o2 = ps.map(q => { const nq = q.match(I18N.NUM) || [], kq = q.replace(I18N.NUM, "#"); let eq = I18N.d[kq]; if (eq == null && /\\.$/.test(kq) && I18N.d[kq.slice(0, -1)] != null) eq = I18N.d[kq.slice(0, -1)] + "."; if (eq == null) return q; hit++; let j = 0; return eq.replace(/#/g, () => (nq[j++] != null ? nq[j - 1] : "#")); }); if (hit) r = t.replace(k, o2.join(" ")); } if (hit < ps.length && I18N.miss.size < 3000) I18N.miss.add(key); } } /* V310.133 : une phrase faite de plusieurs phrases connues est traduite morceau par morceau */')
open(p, "w", encoding="utf-8").write(s)
w = os.path.join(R, "sw.js"); ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611281030';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
