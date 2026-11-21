from h import *
import sys,math
G0=(-20,-2680); E=(40,-2830); L=math.hypot(E[0]-G0[0],E[1]-G0[1]); u=((E[0]-G0[0])/L,(E[1]-G0[1])/L); o=(-u[1],u[0])
def P(d,lat,y):
  return "[%f,%s,%f]"%(G0[0]+u[0]*d+o[0]*lat, y, G0[1]+u[1]*d+o[1]*lat)
def Pd(dexpr,lat,yexpr):
  return "[%f+%f*(%s)+%f,%s,%f+%f*(%s)+%f]"%(G0[0],u[0],dexpr,o[0]*lat,yexpr,G0[1],u[1],dexpr,o[1]*lat)
GH="const GH=window.__W().GH;const gy=GH(%f,%f);"%(G0[0],G0[1])
S={
"portique":GH+"const d=-30+26*T;return {p:%s,t:%s,fov:62};"%(Pd("d",0,"gy+3.2"),Pd("d+40",0,"gy+5.5")),
"colonnes":GH+"const d=40+20*T;return {p:%s,t:%s,fov:66};"%(Pd("d",-1.5,"gy+1.0"),Pd("d+12",6,"gy+12")),
"statue":GH+"const th=0.5*T;const cx=%f,cz=%f;return {p:[cx+16*Math.cos(2.0+th),gy+5,cz+16*Math.sin(2.0+th)],t:[cx,gy+7,cz],fov:58};"%(G0[0]+u[0]*26+o[0]*22,G0[1]+u[1]*26+o[1]*22),
"envol":GH+"const k=Math.min(1,T/1.6);const e=1-Math.pow(1-k,2);return {p:%s,t:%s,fov:62};"%(Pd("55+28*e",0,"gy+3+24*e"),Pd("130+30*e",0,"gy+6")),
"anneaux":GH+"const d=22+16*T;return {p:%s,t:%s,fov:60};"%(Pd("d",6.5,"gy+3.6"),Pd("d+11",10.5,"gy+4.6")),
}
if __name__=="__main__":
  sel=sys.argv[1].split(','); toffs=[float(x) for x in sys.argv[2].split(',')]
  shots=[]
  for k in sel:
    for t in toffs: shots.append(shot("%s_t%02d"%(k,int(t*10)),S[k],dayT=840,toff=t,wait=1500,js=notraf))
  ev="(()=>{const W=window.__W();return {models:Object.keys(W.MODELS||{}).filter(k=>/rex/.test(k))}})()"
  print(run(shots,'/root/cap/s4',ev=ev,wait=False))
