import sys,glob
from PIL import Image
d,out=sys.argv[1],sys.argv[2]; items=sys.argv[3].split(',')  # nm:start:end:step
fs=[]
for it in items:
  nm,a,b,st=it.split(':'); L=sorted(glob.glob(f"{d}/{nm}_*.png"))[int(a):int(b):int(st)]; fs+=L
cols=int(sys.argv[4]) if len(sys.argv)>4 else 8; W_,H_=180,320
rows=(len(fs)+cols-1)//cols; m=Image.new('RGB',(W_*cols,H_*rows))
for i,f in enumerate(fs): m.paste(Image.open(f).convert('RGB').resize((W_,H_)),((i%cols)*W_,(i//cols)*H_))
m.save(out); print(out,len(fs))
