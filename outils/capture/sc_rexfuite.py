# repérage : python3 sc.py <fichier plans> <dossier> nom:clé:n:o,...  → planche
import sys,os,glob
exec(open('/root/w/rx/lib.py').read())
exec(open(sys.argv[1]).read())
out=sys.argv[2]; os.makedirs(out,exist_ok=True)
sh=[]
for it in sys.argv[3].split(','):
  nm,k,n,o=it.split(':'); s=MK(nm,S[k],n=int(n),o=float(o)); s["fps"]=int(os.environ.get("FPS","30")); s["pre"]=int(os.environ.get("PRE","3")); sh.append(s)
run(sh,out,w=1080,h=1920,name="sc%d"%int(time.time()*10))
from PIL import Image
names=[it.split(':')[0] for it in sys.argv[3].split(',')]
fs=[]
for nm in names: fs+=sorted(glob.glob(out+"/"+nm+"_*.png"))
step=int(os.environ.get("STEP","1")); fs=fs[::step]
cols=min(len(fs),int(os.environ.get("COLS","6"))); rows=(len(fs)+cols-1)//cols
W_,H_=270,480
m=Image.new('RGB',(W_*cols,H_*rows))
for i,f in enumerate(fs): m.paste(Image.open(f).convert('RGB').resize((W_,H_)),((i%cols)*W_,(i//cols)*H_))
m.save(out+'.jpg'); print(out+'.jpg',len(fs))
