import sys,math; sys.path.insert(0,'/root/cap')
from h import *
a0=-math.pi*0.62; dx,dz=math.cos(a0),math.sin(a0); px,pz=-dz,dx
hx=-175-dx*36; hz=985-dz*36
def at(d,p): return (hx+dx*d+px*p, hz+dz*d+pz*p)
def J(d,p,y): x,z=at(d,p); return "[%f,%s,%f]"%(x,y,z)
def Jd(dexp,pexp,yexp): return "[%f+%f*(%s)+%f*(%s),%s,%f+%f*(%s)+%f*(%s)]"%(hx,dx,dexp,px,pexp,yexp,hz,dz,dexp,pz,pexp)
GH="const GH=window.__W().GH;const gy=GH(%f,%f);"%(hx,hz)
S={
"S1":(62,GH+"return {p:%s,t:%s,fov:62};"%(Jd("175-38*T","0","gy+60-9*T"),Jd("5","0","gy+2"))),
"S2":(47,GH+"return {p:%s,t:%s,fov:60};"%(Jd("-14","-10+9*T","gy+3"),Jd("40","0","gy+6"))),
"S3":(47,GH+"return {p:%s,t:%s,fov:62};"%(Jd("10+14*T","-6","gy+3.5"),Jd("22+14*T","-45","gy+10"))),
"S4":(47,GH+"const th=0.25*T;return {p:%s,t:%s,fov:66};"%(Jd("55+6*T","8","gy+2"),Jd("0","-10+25*T","gy+38"))),
"S5":(47,GH+"const k=Math.min(1,T/1.5),e=1-Math.pow(1-k,2);return {p:%s,t:%s,fov:60};"%(Jd("-40-50*e","20+30*e","gy+30+40*e"),Jd("50","0","gy"))),
}
if __name__=="__main__":
  sel=sys.argv[1].split(','); mode=sys.argv[2]
  NOPAN="{const e=document.getElementById('screen');if(e){e.classList.add('hidden');e.innerHTML='';}}"
  shots=[]
  for k in sel:
    n,b=S[k]
    if mode=='r':
      for t in (0.1,(n-1)/30): shots.append(shot("%s_t%02d"%(k,int(t*10)),b,dayT=840,toff=t,wait=1500,js=notraf+NOPAN))
    else: shots.append(shot("st_"+k,b,dayT=840,n=n,wait=2500,js=notraf+NOPAN))
  out='/root/cap/st'+('f' if mode=='f' else 'r')
  print(run(shots,out,w=1080 if mode=='f' else 540,h=1920 if mode=='f' else 960,wait=False))
