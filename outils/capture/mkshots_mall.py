import sys; sys.path.insert(0,'/root/cap')
from h import *
MX,MZ=330,1082
S={
"M1":(62,"return {p:[%f-20+8*T,34-9*T,%f-150+38*T],t:[%f,6,%f-40],fov:62};"%(MX,MZ,MX,MZ)),
"M2":(47,"return {p:[%f-75+34*T,3.4,%f-6],t:[%f-55+34*T,3.6,%f+6],fov:66};"%(MX,MZ,MX,MZ)),
"M3":(47,"const th=0.3+0.55*T;return {p:[%f+14*Math.cos(th),5.5,%f+14*Math.sin(th)],t:[%f,2.5,%f],fov:60};"%(MX,MZ,MX,MZ)),
"M4":(47,"return {p:[%f+40-30*T,3.0,%f+12],t:[%f+20-30*T,3.5,%f+25],fov:64};"%(MX,MZ,MX,MZ)),
"M5":(47,"const k=Math.min(1,T/1.5),e=1-Math.pow(1-k,2);return {p:[%f+110+30*e,60+40*e,%f-120-40*e],t:[%f,5,%f],fov:60};"%(MX,MZ,MX,MZ)),
}
sel=sys.argv[1].split(','); mode=sys.argv[2]
shots=[]
NOPAN="{const e=document.getElementById('screen');if(e){e.classList.add('hidden');e.innerHTML='';}}"
for k in sel:
  n,b=S[k]
  if mode=='r':
    for t in (0.1,(n-1)/30): shots.append(shot("%s_t%02d"%(k,int(t*10)),b,dayT=840,toff=t,wait=1500,js=notraf+NOPAN))
  else: shots.append(shot("mall_"+k,b,dayT=840,n=n,wait=2500,js=notraf+NOPAN))
out='/root/cap/mall'+('f' if mode=='f' else 'r')
print(run(shots,out,w=1080 if mode=='f' else 540,h=1920 if mode=='f' else 960,wait=False))
