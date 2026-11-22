# fabrique une page de test locale depuis la source : three.js local, formulaires Google coupés
python3 - "$1" "$2" <<'PY'
import sys
src,out=sys.argv[1],sys.argv[2]; s=open(src).read()
s=s.replace('https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js','node_modules/three/build/three.min.js').replace('https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/','node_modules/three/examples/js/')
s=s.replace('const GFORM = "https://docs.google.com/forms/','const GFORM = "" && "https://docs.google.com/forms/').replace('const GFORM_SCORES = "https://','const GFORM_SCORES = "" && "https://')
open(out,'w').write(s)
PY
