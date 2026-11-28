# enc.py <dossier png> <nom_shot> <sortie.mp4> [flash]
import sys,glob,subprocess,os
from PIL import Image
d,nm,out=sys.argv[1:4]; flash=len(sys.argv)>4
fs=sorted(glob.glob(f"{d}/{nm}_*.png"))
if flash:
  td=f"{d}/_fl_{nm}"; os.makedirs(td,exist_ok=True)
  for i,f in enumerate(fs):
    t=i/60; a=0.9 if t<0.05 else max(0,0.9*(1-(t-0.05)/0.45))
    im=Image.open(f).convert('RGB')
    if a>0: im=Image.blend(im,Image.new('RGB',im.size,(255,255,255)),a)
    im.save(f"{td}/f_{i:03d}.png")
  pat=f"{td}/f_%03d.png"
else:
  pat=f"{d}/{nm}_%03d.png"
subprocess.run(["ffmpeg","-v","error","-y","-framerate","60","-i",pat,"-f","lavfi","-i","anullsrc=r=48000:cl=stereo","-shortest","-c:v","libx264","-crf","14","-preset","veryfast","-pix_fmt","yuv420p","-c:a","aac",out],check=True)
print(out,len(fs))
