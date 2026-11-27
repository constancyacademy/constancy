# V310.121 · GLISSIÈRES DES PONTS (retour de Thomas du 26/11 10h01 : « bordures des ponts qui cassent l'inertie : glisser le long, choc, vibration, secousse »)
# Avant : contre la glissière d'un tablier, la voiture était recollée au bord et perdait 20 % de sa vitesse À CHAQUE IMAGE (à 60 i/s, plus rien en un quart de seconde)
# Après : la perte dépend de l'angle du choc, une seule fois par contact (frôler = presque rien, de face = gros freinage), la voiture glisse le long et son cap se recale sur la glissière
# · au premier contact : bruit de choc à la force du choc, vibration du téléphone, secousse de l'écran · stat glissiere-choc (une fois par partie)
import re, sys
p = "index.html"; s = open(p, encoding="utf-8").read(); n = 0
def rep(a, b):
    global s, n
    if s.count(a) != 1: sys.exit("REFUS %d : %s" % (s.count(a), a[:90]))
    s = s.replace(a, b); n += 1
rep("else if (Math.abs(off) < lim + 3 && (!best || Math.abs(off) - lim < best.e)) best = { e: Math.abs(off) - lim, px, pz, nx, nz, k: Math.sign(off) * lim }; } });",
    "else if (Math.abs(off) < lim + 3 && (!best || Math.abs(off) - lim < best.e)) best = { e: Math.abs(off) - lim, px, pz, nx, nz, tx: vx / l, tz: vz / l, k: Math.sign(off) * lim }; } });")
rep("if (!inside && best) { G.car.x = best.px + best.nx * best.k; G.car.z = best.pz + best.nz * best.k; if (Math.abs(G.car.v) > 8) { if (typeof clang === \"function\") clang(0.4); G.car.v *= 0.8; } } } }",
    "if (!inside && best) { G.car.x = best.px + best.nx * best.k; G.car.z = best.pz + best.nz * best.k; /* V310.121 (Thomas : « les bordures des ponts cassent l'inertie ») : la voiture glisse le long de la glissière, perte selon l'angle et une seule fois par contact, choc, vibration, secousse */\n"
    "      const c = G.car, fx = Math.sin(c.h), fz = Math.cos(c.h), dp = fx * best.tx + fz * best.tz, sa = Math.sqrt(Math.max(0, 1 - dp * dp)), av = Math.abs(c.v), now = performance.now();\n"
    "      if (!DK.railT || now - DK.railT > 700) { if (av > 4) { c.v *= 1 - Math.min(0.5, Math.max(0.02, sa * sa * 0.7)); const k = Math.min(1, av * (0.25 + sa) / 30); try { if (typeof clang === \"function\") clang(Math.max(0.15, k)); } catch (e) {} try { navigator.vibrate && navigator.vibrate(k > 0.5 ? [30, 30, 40] : 25); } catch (e) {} try { shakeAdd(Math.min(0.7, 0.12 + k * 0.6)); } catch (e) {} if (!DK.railS) { DK.railS = 1; try { stat(\"glissiere-choc\"); } catch (e) {} } } }\n"
    "      DK.railT = now; if (av > 1 && sa > 0.02) { const sg = (dp * (c.v >= 0 ? 1 : -1)) >= 0 ? 1 : -1, ht = Math.atan2(best.tx * sg, best.tz * sg); let d = ht - c.h; while (d > Math.PI) d -= 2 * Math.PI; while (d < -Math.PI) d += 2 * Math.PI; if (c.v < 0) { d = ht + Math.PI - c.h; while (d > Math.PI) d -= 2 * Math.PI; while (d < -Math.PI) d += 2 * Math.PI; } c.h += d * Math.min(1, dt * 7); } } } }")
open(p, "w", encoding="utf-8").write(s)
w = "sw.js"; ws = open(w, encoding="utf-8").read(); ws2 = re.sub(r"const V = 'constancy-\d+';", "const V = 'constancy-202611272215';", ws, count=1); assert ws2 != ws; open(w, "w", encoding="utf-8").write(ws2)
print("OK", n, "remplacements")
