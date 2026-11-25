import sys,subprocess,numpy as np
# usage: v4.py interp60.mp4 orig30.mp4 out.mp4 "a-b,c-d" (plages d'images 60 i/s en doublement)
I,O,OUT,R=sys.argv[1:5]
dup=set()
for r in R.split(','):
  a,b=map(int,r.split('-')); dup|=set(range(a,b+1))
def frames(path,w,h,fmt,extra=''):
  vf=('scale=%d:%d,'%(w,h) if w!=1080 else '')+'format='+fmt
  p=subprocess.Popen(['ffmpeg','-v','error','-i',path,'-vf',vf,'-f','rawvideo','-'],stdout=subprocess.PIPE)
  ch=1 if fmt=='gray' else 3; n=w*h*ch
  while True:
    b=p.stdout.read(n)
    if len(b)<n: break
    yield np.frombuffer(b,np.uint8).reshape(h,w,ch) if ch>1 else np.frombuffer(b,np.uint8).reshape(h,w)
# 1) netteté de chaque image interpolée (540 x 960, 12-62 % de la hauteur)
sh=[];sm=[]
for f in frames(I,540,960,'gray'):
  sm.append(f[::8,::8].astype(np.float32))
  g=f[115:595].astype(np.float32)
  lap=np.abs(4*g[1:-1,1:-1]-g[:-2,1:-1]-g[2:,1:-1]-g[1:-1,:-2]-g[1:-1,2:])
  sh.append(lap.mean())
sh=np.array(sh); N=len(sh)
bad=set();chg=set()
for i in range(1,N-1):
  if i%2==1 and i not in dup and sh[i]/((sh[i-1]+sh[i+1])/2+1e-6)<0.90: bad.add(i)
  if i%2==1 and i not in dup:
    d=np.abs(sm[i+1]-sm[i-1]); H,Wd=d.shape
    blk=max(d[y:y+H//8,x:x+Wd//4].mean() for y in range(0,H-H//8+1,H//8) for x in range(0,Wd-Wd//4+1,Wd//4))
    if blk>80: bad.add(i); chg.add(i)
# 2) composition : doublement (image 30 i/s floor(i/2)) · image inventée floue -> copie de l'image d'avant
oi=frames(I,1080,1920,'rgb24'); oo=frames(O,1080,1920,'rgb24')
enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1920','-r','60','-i','-','-i',O,'-map','0:v','-map','1:a','-c:v','libx264','-crf','16','-preset','medium','-pix_fmt','yuv420p','-c:a','copy','-movflags','+faststart',OUT],stdin=subprocess.PIPE)
prev=None; cur30=None; k30=-1
for i in range(N):
  fi=next(oi)
  while k30<i//2: cur30=next(oo); k30+=1
  if i in dup: fr=cur30
  elif i in bad: fr=prev
  else: fr=fi
  enc.stdin.write(fr.tobytes()); prev=fr
enc.stdin.close(); enc.wait()
print(OUT,'coupes/changements',sorted(chg),'images',N,'doublées',len([d for d in dup if d<N]),'remplacées (floues)',sorted(bad))
