# V310.117 (suite) · textes déjà écrits en anglais dans le code (écran de chargement, touches, pub Playgama, Poki) et noms de lieux restés en français, relevés en jeu (window.__i18nMiss2) en espagnol et en allemand
import json
X = {
 "Free open-world city": ["Ciudad de mundo abierto gratis", "Cidade de mundo aberto grátis", "Kostenlose Open-World-Stadt"],
 "Loading the city ·": ["Cargando la ciudad ·", "Carregando a cidade ·", "Stadt wird geladen ·"],
 "Your first delivery is waiting.": ["Tu primera entrega te espera.", "Sua primeira entrega está esperando.", "Deine erste Lieferung wartet."],
 "Earn your first car. Then a better one.": ["Gánate tu primer coche. Y luego uno mejor.", "Conquiste seu primeiro carro. Depois um melhor.", "Verdien dir dein erstes Auto. Dann ein besseres."],
 "Free. No download. No account.": ["Gratis. Sin descarga. Sin cuenta.", "Grátis. Sem download. Sem conta.", "Gratis. Kein Download. Kein Konto."],
 "or": ["o", "ou", "oder"], "Arrows": ["Flechas", "Setas", "Pfeiltasten"], "Space": ["Espacio", "Espaço", "Leertaste"],
 "· Drive & walk": ["· Conducir y caminar", "· Dirigir e andar", "· Fahren & gehen"], "· Brake": ["· Frenar", "· Frear", "· Bremsen"], "· Get in / out": ["· Subir / bajar", "· Entrar / sair", "· Ein- / Aussteigen"], "· Run": ["· Correr", "· Correr", "· Rennen"],
 "drive ·": ["conducir ·", "dirigir ·", "fahren ·"], "brake ·": ["frenar ·", "frear ·", "bremsen ·"], "get in / out ·": ["subir / bajar ·", "entrar / sair ·", "ein- / aussteigen ·"], "run": ["correr", "correr", "rennen"],
 "Thumb at the bottom of the screen · Slide up to go": ["Pulgar abajo en la pantalla · Desliza hacia arriba para avanzar", "Polegar embaixo na tela · Deslize para cima para ir", "Daumen unten auf den Bildschirm · Nach oben wischen zum Losfahren"],
 "Menu": ["Menú", "Menu", "Menü"], "Horn": ["Claxon", "Buzina", "Hupe"], "Radio": ["Radio", "Rádio", "Radio"], "Muscle": ["Músculo", "Músculos", "Muskeln"], "Business": ["Negocio", "Negócios", "Business"], "Mindset": ["Mentalidad", "Mentalidade", "Mindset"],
 "Free Fall": ["Caída libre", "Queda livre", "Freier Fall"], "Garage": ["Garaje", "Garagem", "Garage"], "Pop-corn": ["Palomitas", "Pipoca", "Popcorn"], "Hot-dogs": ["Perritos", "Cachorro-quente", "Hotdogs"], "Carrousel": ["Tiovivo", "Carrossel", "Karussell"],
 "Tone #": ["Tono #", "Tom #", "Ton #"], "Grab the cash.": ["Coge el dinero.", "Pegue a grana.", "Schnapp dir das Geld."], "Your first delivery pays for a better car.": ["Tu primera entrega paga un coche mejor.", "Sua primeira entrega paga um carro melhor.", "Deine erste Lieferung bezahlt ein besseres Auto."],
 "Marine Agency": ["Agencia Náutica", "Agência Náutica", "Marine-Agentur"], "Airline Agency": ["Agencia de aviones", "Agência aérea", "Airline-Agentur"], "Constancy Gym": ["Gimnasio Constancy", "Academia Constancy", "Constancy Gym"], "Beach Bar · Flamingo": ["Chiringuito · Flamingo", "Bar de praia · Flamingo", "Strandbar · Flamingo"],
 "Terminal # · International": ["Terminal # · Internacional", "Terminal # · Internacional", "Terminal # · International"], "Tennis · Half-pipe": ["Tenis · Half-pipe", "Tênis · Half-pipe", "Tennis · Halfpipe"],
 "▶ Watch an ad · +$#": ["▶ Ver un anuncio · +$#", "▶ Ver um anúncio · +$#", "▶ Werbung ansehen · +$#"], "▶ Watch an ad · Start with +$#": ["▶ Ver un anuncio · Empieza con +$#", "▶ Ver um anúncio · Comece com +$#", "▶ Werbung ansehen · Start mit +$#"],
 "Loading the ad…": ["Cargando el anuncio…", "Carregando o anúncio…", "Werbung wird geladen…"], "✓ +$# waiting for you in the game": ["✓ +$# te esperan en el juego", "✓ +$# te esperando no jogo", "✓ +$# warten im Spiel auf dich"], "Ad not available right now": ["Anuncio no disponible ahora", "Anúncio indisponível agora", "Werbung gerade nicht verfügbar"],
 "· Thanks for watching!": ["· ¡Gracias por verlo!", "· Valeu por assistir!", "· Danke fürs Zuschauen!"], "▶ PLAY": ["▶ JUGAR", "▶ JOGAR", "▶ SPIELEN"], "Tap to play": ["Toca para jugar", "Toque para jogar", "Tippen zum Spielen"],
}
en = json.load(open("assets/i18n/en.json", encoding="utf-8")); en.setdefault("Ton #", "Tone #"); en.setdefault("Agence Marine", "Marine Agency"); json.dump(en, open("assets/i18n/en.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
for k, L in enumerate(["es", "pt", "de"]):
    f = "assets/i18n/%s.json" % L; d = json.load(open(f, encoding="utf-8"))
    for e, v in X.items():
        assert e.count("#") == v[k].count("#"), (e, v[k]); d[e] = v[k]
    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":")); print(L, len(d))
