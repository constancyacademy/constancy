import sys,os,glob,time
exec(open('/root/w/cy/lib.py').read())
exec(open(sys.argv[1]).read())
out=sys.argv[2]; os.makedirs(out,exist_ok=True)
sh=[]
for it in sys.argv[3].split(','):
  nm,k,n,o=it.split(':'); s=MK(nm,S[k],n=int(n),o=float(o)); s["fps"]=int(os.environ.get("FPS","30")); s["pre"]=int(os.environ.get("PRE","3"))
  if k in DTS: s["dayT"]=DTS[k]
  sh.append(s)
run(sh,out,w=1080,h=1920,name="sc%d"%int(time.time()*10))
from PIL import Image
names=[it.split(':')[0] for it in sys.argv[3].split(',')]
fs=[]
for nm in names: fs+=sorted(glob.glob(out+"/"+nm+"_*.png"))
cols=min(len(fs),int(os.environ.get("COLS","6"))); rows=(len(fs)+cols-1)//cols
m=Image.new('RGB',(270*cols,480*rows))
for i,f in enumerate(fs): m.paste(Image.open(f).convert('RGB').resize((270,480)),((i%cols)*270,(i//cols)*480))
m.save(out+'.jpg'); print(out+'.jpg',len(fs))
