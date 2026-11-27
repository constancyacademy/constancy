# V310.132 · textes encore en français sur les plateformes : écran « Quit game » et notification « Défi du jour » (+ es, pt, de)
import json, os
EN = {
 "Changer d'objectif": "Change goal",
 "Retour": "Back",
 "Mon code de partie": "My game code",
 "Pour retrouver ta partie sur un autre appareil.": "To get your game back on another device.",
 "Ta partie est gardée en ligne. Tu la retrouves avec « J'ai déjà un compte », sur n'importe quel appareil.": "Your game is kept online. Get it back with “I already have an account”, on any device.",
 "Défi du jour · Code de la route.": "Today's challenge · Rules of the road.",
 "Défi du jour · Conduite propre.": "Today's challenge · Clean driving.",
 "Défi du jour · Marche quotidienne.": "Today's challenge · Daily walk.",
 "Défi du jour · Routine du matin.": "Today's challenge · Morning routine.",
 "Défi du jour · Déménagement express.": "Today's challenge · Express move.",
 "Il change chaque jour. # jours d'affilée = gros bonus.": "It changes every day. # days in a row = big bonus.",
}
X = {
 "es": {"Change goal": "Cambiar de objetivo", "Back": "Volver", "My game code": "Mi código de partida", "To get your game back on another device.": "Para recuperar tu partida en otro dispositivo.", "Your game is kept online. Get it back with “I already have an account”, on any device.": "Tu partida se guarda en línea. Recupérala con «Ya tengo una cuenta», en cualquier dispositivo.", "Today's challenge · Rules of the road.": "Reto del día · Código de circulación.", "Today's challenge · Clean driving.": "Reto del día · Conducción limpia.", "Today's challenge · Daily walk.": "Reto del día · Paseo diario.", "Today's challenge · Morning routine.": "Reto del día · Rutina de la mañana.", "Today's challenge · Express move.": "Reto del día · Mudanza exprés.", "It changes every day. # days in a row = big bonus.": "Cambia cada día. # días seguidos = gran bonus.", "Ad closed · no reward this time.": "Anuncio cerrado · esta vez sin recompensa."},
 "pt": {"Change goal": "Mudar de objetivo", "Back": "Voltar", "My game code": "Meu código de jogo", "To get your game back on another device.": "Para recuperar seu jogo em outro aparelho.", "Your game is kept online. Get it back with “I already have an account”, on any device.": "Seu jogo fica salvo online. Recupere com “Já tenho uma conta”, em qualquer aparelho.", "Today's challenge · Rules of the road.": "Desafio do dia · Leis de trânsito.", "Today's challenge · Clean driving.": "Desafio do dia · Direção limpa.", "Today's challenge · Daily walk.": "Desafio do dia · Caminhada diária.", "Today's challenge · Morning routine.": "Desafio do dia · Rotina da manhã.", "Today's challenge · Express move.": "Desafio do dia · Mudança expressa.", "It changes every day. # days in a row = big bonus.": "Muda todo dia. # dias seguidos = grande bônus.", "Ad closed · no reward this time.": "Anúncio fechado · sem recompensa desta vez."},
 "de": {"Change goal": "Ziel ändern", "Back": "Zurück", "My game code": "Mein Spielcode", "To get your game back on another device.": "Um dein Spiel auf einem anderen Gerät wiederzufinden.", "Your game is kept online. Get it back with “I already have an account”, on any device.": "Dein Spiel bleibt online gespeichert. Hol es dir mit „Ich habe schon ein Konto“ zurück, auf jedem Gerät.", "Today's challenge · Rules of the road.": "Tagesaufgabe · Verkehrsregeln.", "Today's challenge · Clean driving.": "Tagesaufgabe · Sauber fahren.", "Today's challenge · Daily walk.": "Tagesaufgabe · Täglicher Spaziergang.", "Today's challenge · Morning routine.": "Tagesaufgabe · Morgenroutine.", "Today's challenge · Express move.": "Tagesaufgabe · Express-Umzug.", "It changes every day. # days in a row = big bonus.": "Sie wechselt jeden Tag. # Tage am Stück = großer Bonus.", "Ad closed · no reward this time.": "Werbung geschlossen · diesmal keine Belohnung."},
}
def upd(f, D):
    d = json.load(open(f, encoding="utf-8")); n = 0
    for k, v in D.items():
        if d.get(k) != v: d[k] = v; n += 1
    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":")); return n
print("en", upd("assets/i18n/en.json", EN))
for L, D in X.items(): print(L, upd("assets/i18n/%s.json" % L, D))
