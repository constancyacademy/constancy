#!/bin/bash
# VERROU DU MONTEUR · Une seule session du monteur à la fois (règle de Thomas du 20/11/2026).
# Le verrou est le fichier verrou/VERROU de la branche « rushes ». Le push git est atomique :
# si deux sessions le prennent en même temps, une seule réussit, l'autre est refusée.
# Usage :
#   bash outils/verrou.sh prendre            → 0 si le verrou est à toi, 3 si une autre session monte
#   bash outils/verrou.sh rafraichir         → repousse l'échéance de ton verrou (appelé par render2.py)
#   bash outils/verrou.sh deposer "<texte>"  → dépose ton message dans la file (session bloquée)
#   bash outils/verrou.sh rendre             → libère le verrou (refusé s'il reste des messages en file)
#   bash outils/verrou.sh etat               → affiche qui a le verrou
R=$(cd "$(dirname "$0")/.." && pwd)
# Le verrou vit dans un clone à part ($HOME/.verrou), pour ne jamais toucher aux rushes en cours de la session.
VR=$HOME/.verrou
if [ ! -d "$VR/.git" ]; then
  URL=$(git -C "$R" remote get-url origin)
  git clone -q --depth 1 --filter=blob:none --sparse -b rushes "$URL" "$VR" || { echo "Erreur : clone du verrou impossible."; exit 1; }
  git -C "$VR" sparse-checkout set verrou >/dev/null 2>&1
fi
cd "$VR" || exit 1
DUREE=${VERROU_DUREE:-4500}          # 75 min, repoussé à chaque montage
SF=$HOME/.monteur_session
[ -s "$SF" ] || echo "monteur-$(date +%s)-$RANDOM$RANDOM" > "$SF"
MOI=$(cat "$SF")
git config user.email >/dev/null || git config user.email "monteur@constancy.fr"
git config user.name  >/dev/null || git config user.name  "Monteur Constancy"

maj() { git fetch -q --depth 1 origin rushes && git reset -q --hard FETCH_HEAD; }
lire() { # session, pris, echeance
  if [ -f verrou/VERROU ]; then
    S=$(sed -n 's/^session=//p' verrou/VERROU); P=$(sed -n 's/^pris=//p' verrou/VERROU); E=$(sed -n 's/^echeance=//p' verrou/VERROU)
  else S=""; P=0; E=0; fi
}
heure() { TZ=Europe/Paris date -d "@$1" +%Hh%M; }
ecrire() { mkdir -p verrou; NOW=$(date +%s)
  printf 'session=%s\npris=%s\necheance=%s\n' "$MOI" "${1:-$NOW}" "$((NOW+DUREE))" > verrou/VERROU
  git add verrou/VERROU && git commit -q -m "$2" && git push -q origin HEAD:rushes; }
file_attente() { ls verrou/file/*.txt 2>/dev/null; }

case "$1" in
prendre)
  for i in 1 2 3 4; do
    maj || { echo "Erreur : branche rushes injoignable."; exit 1; }
    lire; NOW=$(date +%s)
    if [ -n "$S" ] && [ "$S" != "$MOI" ] && [ "$E" -gt "$NOW" ]; then
      echo "=================================================================="
      echo "STOP · UNE AUTRE SESSION DU MONTEUR TRAVAILLE DÉJÀ (verrou pris à $(heure $P), libre au plus tard à $(heure $E))."
      echo "Ne monte RIEN, ne filme RIEN, ne relis aucun doc. Fais seulement ceci, puis arrête-toi :"
      echo "1. Si un message t'a lancé (expert, conversation jeu), dépose-le mot pour mot :"
      echo "   bash $R/outils/verrou.sh deposer \"<le message>\""
      echo "   La session en cours le traitera avant de finir. Rien n'est perdu."
      echo "2. Réponse finale : « RAS · Une autre session du monteur travaille, message déposé dans la file. »"
      echo "=================================================================="
      exit 3
    fi
    if ecrire "" "Verrou du monteur pris ($MOI)"; then
      echo "VERROU PRIS : Tu es la seule session du monteur jusqu'à $(heure $((NOW+DUREE))) (repoussé à chaque montage)."
      if [ -n "$(file_attente)" ]; then
        echo "MESSAGES EN ATTENTE DANS LA FILE (à traiter EN PREMIER, avant tout le reste) :"
        for f in $(file_attente); do echo "--- $(basename "$f")"; cat "$f"; echo; done
      fi
      exit 0
    fi
    sleep $((RANDOM % 5 + 2))   # push refusé : une autre session vient d'écrire, on relit
  done
  echo "STOP · Verrou impossible à prendre (conflits répétés). Réponse finale : « RAS · verrou occupé. »"; exit 3 ;;
rafraichir)
  maj >/dev/null 2>&1 || exit 0; lire
  [ "$S" = "$MOI" ] || exit 0
  NOW=$(date +%s); [ $((E-NOW)) -lt 2700 ] && ecrire "$P" "Verrou du monteur prolongé ($MOI)" >/dev/null 2>&1
  exit 0 ;;
deposer)
  shift; maj || exit 1; mkdir -p verrou/file
  F=verrou/file/$(date +%s)-$RANDOM.txt
  printf '%s · %s\n%s\n' "$(TZ=Europe/Paris date '+%d/%m %Hh%M')" "$MOI" "$*" > "$F"
  for i in 1 2 3; do git add "$F" && git commit -q -m "File du monteur : message déposé" && git push -q origin HEAD:rushes && { echo "Message déposé dans la file."; exit 0; }
    F2=$(cat "$F" 2>/dev/null); maj; mkdir -p verrou/file; printf "%s" "$F2" > "$F"; done
  echo "Erreur : dépôt impossible."; exit 1 ;;
rendre)
  maj || exit 1; lire
  if [ -n "$(file_attente)" ] && [ "$S" = "$MOI" ]; then
    echo "PAS ENCORE : Des messages sont arrivés pendant ton travail. Traite-les d'abord :"
    for f in $(file_attente); do echo "--- $(basename "$f")"; cat "$f"; echo; done
    echo "Une fois traités : bash $R/outils/verrou.sh traites, puis relance « rendre »."
    exit 2
  fi
  if [ "$S" = "$MOI" ]; then git rm -q verrou/VERROU && git commit -q -m "Verrou du monteur rendu ($MOI)" && git push -q origin HEAD:rushes && echo "Verrou rendu."; else echo "Ce verrou n'est pas à toi, rien à rendre."; fi ;;
traites)
  maj || exit 1; mkdir -p verrou/fait
  for f in $(file_attente); do git mv "$f" verrou/fait/; done
  git commit -q -m "File du monteur : messages traités" && git push -q origin HEAD:rushes && echo "Messages marqués traités." ;;
etat)
  maj; lire; NOW=$(date +%s)
  if [ -n "$S" ] && [ "$E" -gt "$NOW" ]; then echo "Verrou pris par $S depuis $(heure $P), échéance $(heure $E)."; else echo "Verrou libre."; fi
  n=$(file_attente | wc -l); echo "Messages en file : $n." ;;
*) echo "Usage : verrou.sh prendre|rafraichir|deposer \"texte\"|rendre|etat"; exit 1 ;;
esac
