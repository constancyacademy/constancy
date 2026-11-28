# V310.133 · textes encore en français vus sur pg par la BUSINESS (28/11 9h50) : fenêtre « Give up the mission? », « Bouge », 1re mission (+ es, pt, de)
import json
EN = {"Je continue": "Keep going", "Abandonner · -$#": "Give up · -$#", "Bouge": "Move"}
X = {"es": {"Keep going": "Sigo", "Give up · -$#": "Abandonar · -$#", "Move": "Muévete", "Deliver your first kebab. The GPS is set, follow the line on the map.": "Entrega tu primer kebab. El GPS está listo, sigue la línea en el mapa."},
     "pt": {"Keep going": "Vou continuar", "Give up · -$#": "Desistir · -$#", "Move": "Mexa-se", "Deliver your first kebab. The GPS is set, follow the line on the map.": "Entregue seu primeiro kebab. O GPS está pronto, siga a linha no mapa."},
     "de": {"Keep going": "Weitermachen", "Give up · -$#": "Aufgeben · -$#", "Move": "Beweg dich", "Deliver your first kebab. The GPS is set, follow the line on the map.": "Liefere deinen ersten Kebab. Das GPS ist eingestellt, folge der Linie auf der Karte."}}
def upd(f, D):
    d = json.load(open(f, encoding="utf-8")); n = 0
    for k, v in D.items():
        if d.get(k) != v: d[k] = v; n += 1
    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":")); return n
print("en", upd("assets/i18n/en.json", EN))
for L, D in X.items(): print(L, upd("assets/i18n/%s.json" % L, D))
# 133d : première livraison évidente
EN2 = {"Livre ta première commande · suis la flèche violette": "Deliver your first order · Follow the purple arrow", "Glisse le pouce vers le haut pour rouler. Suis la flèche violette.": "Slide your thumb up to drive. Follow the purple arrow.", "Reste appuyé sur ↑ ou W pour rouler. Suis la flèche violette.": "Hold ↑ or W to drive. Follow the purple arrow."}
X2 = {"es": {"Deliver your first order · Follow the purple arrow": "Entrega tu primer pedido · Sigue la flecha morada", "Slide your thumb up to drive. Follow the purple arrow.": "Desliza el pulgar hacia arriba para conducir. Sigue la flecha morada.", "Hold ↑ or W to drive. Follow the purple arrow.": "Mantén ↑ o W para conducir. Sigue la flecha morada."},
      "pt": {"Deliver your first order · Follow the purple arrow": "Entregue seu primeiro pedido · Siga a seta roxa", "Slide your thumb up to drive. Follow the purple arrow.": "Deslize o polegar para cima para dirigir. Siga a seta roxa.", "Hold ↑ or W to drive. Follow the purple arrow.": "Segure ↑ ou W para dirigir. Siga a seta roxa."},
      "de": {"Deliver your first order · Follow the purple arrow": "Liefere deine erste Bestellung · Folge dem lila Pfeil", "Slide your thumb up to drive. Follow the purple arrow.": "Schieb den Daumen nach oben, um zu fahren. Folge dem lila Pfeil.", "Hold ↑ or W to drive. Follow the purple arrow.": "Halte ↑ oder W gedrückt, um zu fahren. Folge dem lila Pfeil."}}
print("en", upd("assets/i18n/en.json", EN2))
for L, D in X2.items(): print(L, upd("assets/i18n/%s.json" % L, D))
