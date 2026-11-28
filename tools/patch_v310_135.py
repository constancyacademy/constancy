# V310.135 · COMMANDE DE LA BUSINESS DU 28/11 12H50 (claude/constancy-commande-chargement-rejoins-moi-28-11.txt), point 1 · CRAZYGAMES, TEMPS JUSQU'AU DÉBUT DU JEU
# Mesuré avant de coder (zip cg V310.134, cloud sans carte graphique) : fichiers reçus à 4,3 s, construction de la ville 11,7 s (dont sol du continent 3,3 s, campagne 2,7 s, régions),
# compilation des shaders 1,5 s, puis le miroir du perso (rendu 3D de l'avatar, 36 images) que personne ne voit sur une plateforme + l'animation « Bienvenue » de 2,25 s avant l'entrée en jeu.
# 1. Plateformes, nouvelle partie : plus de miroir ni d'animation invisibles, l'objectif Cash et le perso par défaut sont posés directement (même résultat que le miroir automatique de la V310.75)
# 2. CrazyGames : le sol du continent à plus de 900 m du départ et la campagne se construisent après l'entrée en jeu, une dalle à la fois (pas d'à-coup)
# 3. Flèche de la 1re livraison : aussi pour la livraison du kebab (vue sans flèche par la BUSINESS dans l'aperçu CrazyGames) · « Follow the dot purple dot on the map. » corrigé
import os, re
R = os.getcwd(); p = os.path.join(R, "index.html"); s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: raise SystemExit("REFUS : texte de départ trouvé %d fois : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
# 1. miroir sauté sur les plateformes
rep('else { createAvatar(); if (G.pfast) portalAutoAvatar(); }',
    'else if (G.pfast && PORTAL && !CREATOR) { /* V310.135 : sur une plateforme, le miroir (rendu 3D du perso) et « Bienvenue » ne se voyaient pas et coûtaient plusieurs secondes · même résultat : perso par défaut, objectif Cash */ try { MOBJ.k = "cash"; stat("perso-cree"); stat("portail-miroir-direct"); afterAvatar(); } catch (e) { console.warn("miroir direct", e); createAvatar(); portalAutoAvatar(); } } else { createAvatar(); if (G.pfast) portalAutoAvatar(); }')
# 2a. campagne après l'entrée en jeu sur cg
rep('zones: ["mont", "parc", "lieux"], w: [] };', 'zones: ["mont", "parc", "lieux", "campagne"], w: [], tiles: [] };')
# 2b. dalles lointaines du continent après l'entrée en jeu sur cg
rep('function buildContinent() { if (CONT.built || !CONT.on) return; CONT.built = true; CONT.tiles = []; const TS = 480, SEG = 80;',
    'function buildContinent() { if (CONT.built || !CONT.on) return; CONT.built = true; CONT.tiles = []; const TS = 480, SEG = 80;\n'
    '  /* V310.135 · CrazyGames : les dalles de sol à plus de 900 m du départ se construisent après l\'entrée en jeu (3,3 s de calcul en moins au chargement) */ const contTile = (X, Zt, TS, SEG) => { if (CGL.on && Math.hypot(Math.max(0, Math.abs(X + TS / 2) - TS / 2), Math.max(0, Math.abs(Zt + TS / 2) - TS / 2)) > 900) CGL.tiles.push([X, Zt, TS, SEG]); else contTile0(X, Zt, TS, SEG); };')
rep('function contTile(X, Zt, TS, SEG) {', 'function contTile0(X, Zt, TS, SEG) {')
rep('try { runDeferred("all", 250); } catch (e) {} }); }',
    'try { runDeferred("all", 250); } catch (e) {} const tl = () => { const t = CGL.tiles.shift(); if (!t) { try { cullChunks.big = null; } catch (e) {} window.__cgTiles = 1; return; } try { contTile0(t[0], t[1], t[2], t[3]); } catch (e) { console.warn("dalle", e); } setTimeout(tl, 140); }; setTimeout(tl, 400); }); }')
# 3a. flèche aussi pour le kebab (toute 1re livraison)
rep('on = !!(PORTAL && !CREATOR && M && M.r3 && M.type === "livraison" && G.mode === "play"', 'on = !!(PORTAL && !CREATOR && M && M.type === "livraison" && !M.chain && G.mode === "play"')
# 3b. « Suis le point violet » : le mot coloré coupait la phrase en deux pour la traduction
rep('sub = `Suis le point <b style="color:${COL.business}">violet</b> sur la carte.`;', 'sub = `Suis le <b style="color:${COL.business}">point violet</b> sur la carte.`;')
rep('help(`Colis chargé. Suis le point <b style="color:${COL.business}">violet</b>.`);', 'help(`Colis chargé. Suis le <b style="color:${COL.business}">point violet</b>.`);')
open(p, "w", encoding="utf-8").write(s)
w = os.path.join(R, "sw.js"); ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611281330';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
