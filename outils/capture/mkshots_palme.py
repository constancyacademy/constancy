import sys,math; sys.path.insert(0,'/root/cap')
from h import *
S={
"P1":(62,"return {p:[-420-60*T,560-30*T,1000-40*T],t:[-1480,0,300],fov:62};"),
"P2":(47,"return {p:[-640-70*T,90,250],t:[-1200-70*T,20,330],fov:62};"),
"P3":(47,"return {p:[-1500+40*T,1300,1150],t:[-1500,0,330],fov:60};"),
"P4":(47,"return {p:[-1100-40*T,260,-450],t:[-1500,0,330],fov:62};"),
}
S["A"]=(62,"const th=1.15+0.42*T;return {p:[-1500+430*Math.cos(th),1180-70*T,330+430*Math.sin(th)],t:[-1500,0,330],fov:62};")
S["T"]=(47,"return {p:[-650-100*T,85,262],t:[-1150-100*T,25,330],fov:62};")
S["F"]=(31,"const d=60+80*T;return {p:[-1603-0.983*d-0.182*48,34,349+0.182*d-0.983*48],t:[-1603-0.983*(d+90),4,349+0.182*(d+90)],fov:62};")
S["H"]=(47,"return {p:[-1840-55*T,78,300+10*T],t:[-2140,72,330],fov:60};")
S["R"]=(46,"const k=Math.min(1,T/1.5),e=1-Math.pow(1-k,2);return {p:[-1000-60*e,240+120*e,-420-80*e],t:[-1500,0,330],fov:62};")
if __name__=="__main__":
  sel=sys.argv[1].split(','); mode=sys.argv[2]; dt=int(sys.argv[3]) if len(sys.argv)>3 else 630
  NOPAN="{const e=document.getElementById('screen');if(e){e.classList.add('hidden');e.innerHTML='';}}"
  shots=[]
  for k in sel:
    n,b=S[k]
    if mode=='r':
      for t in (0.1,(n-1)/30): shots.append(dict(shot("%s_t%02d"%(k,int(t*10)),b,dayT=dt,toff=t,wait=2500,js=notraf+NOPAN),far=6000))
    else: shots.append(dict(shot("pa_"+k,b,dayT=dt,n=n,wait=3000,js=notraf+NOPAN),far=6000))
  out='/root/cap/pa'+('f' if mode=='f' else 'r')
  print(run(shots,out,w=1080 if mode=='f' else 540,h=1920 if mode=='f' else 960,wait=False))
