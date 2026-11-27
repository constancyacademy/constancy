# V310.107 · 60 IMAGES/S SUR ORDINATEUR (Thomas 27/11 17h03 : « une fois sur deux, on a des images en 30 fps et pas en 60 »)
# 1. définition plafonnée sur ordinateur à ~4,2 millions de pixels rendus (un écran Retina 5K plein écran en rendait jusqu'à 4 fois plus)
# 2. fin du yo-yo : la résolution adaptative remontait d'un cran toutes les 6 s de fluidité, retombait à 30 i/s, redescendait… · un cran qui fait retomber sous 52 i/s dans les 15 s est annulé et devient le plafond de la session (pareil pour le halo)
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep('return Math.min(fine ? 2 : LIGHT ? 1.2 : 1.6, window.devicePixelRatio || 1); }',
    'return Math.min(fine ? 2 : LIGHT ? 1.2 : 1.6, window.devicePixelRatio || 1, fine ? Math.max(1, Math.sqrt(4.2e6 / Math.max(1, innerWidth * innerHeight))) : 9); } /* V310.107 : sur ordinateur, au plus ~4,2 millions de pixels rendus */')
rep('        if (FXR.on && PF.pr <= 1.5 + 0.01) { FXR.on = false; FXR.auto = true; }',
    '        if (PF.up && now - PF.up.t < 15000) { const u = PF.up; PF.up = null; if (u.fx) { FXR.on = false; FXR.auto = true; FXR.fail = true; } else { PF.pr = u.pr; PF.cap = u.pr; renderer.setPixelRatio(PF.pr); fxSize(); } } /* V310.107 : le cran qu\'on vient de monter fait retomber la fluidité → on l\'annule et il devient le plafond (fin du yo-yo 60/30 i/s) */\n        else if (FXR.on && PF.pr <= 1.5 + 0.01) { FXR.on = false; FXR.auto = true; }')
rep('else if (PF.pr < 1.0 - 0.01) { PF.pr = Math.min(1.0, PF.pr + 0.125); renderer.setPixelRatio(PF.pr); fxSize(); } else if (FXR.auto && !FXR.on && !FXR.fail) { FXR.on = true; FXR.auto = false; } else if (PF.pr < hi - 0.01) { PF.pr = Math.min(hi, PF.pr + 0.25); renderer.setPixelRatio(PF.pr); fxSize(); }',
    'else if (PF.pr < Math.min(1.0, PF.cap || 9) - 0.01) { PF.up = { t: now, pr: PF.pr }; PF.pr = Math.min(1.0, PF.cap || 9, PF.pr + 0.125); renderer.setPixelRatio(PF.pr); fxSize(); } else if (FXR.auto && !FXR.on && !FXR.fail) { PF.up = { t: now, fx: 1 }; FXR.on = true; FXR.auto = false; } else if (PF.pr < Math.min(hi, PF.cap || 9) - 0.01) { PF.up = { t: now, pr: PF.pr }; PF.pr = Math.min(hi, PF.cap || 9, PF.pr + 0.25); renderer.setPixelRatio(PF.pr); fxSize(); }')
open(p, "w", encoding="utf-8").write(s)
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611271730';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
