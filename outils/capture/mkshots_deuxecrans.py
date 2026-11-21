import sys,json,math; sys.path.insert(0,'/root/cap'); sys.path.insert(0,'/root/cap/m1')
from h import *
from path import *
# chemins rééchantillonnés à 1 m : [x, z, y]
def resample(P,ycol=True):
  out=[];cum=[0]
  for i in range(1,len(P)): cum.append(cum[-1]+math.hypot(P[i][0]-P[i-1][0],P[i][1]-P[i-1][1]))
  L=cum[-1]; j=0; s=0.0
  while s<=L:
    while j<len(P)-2 and cum[j+1]<s: j+=1
    t=(s-cum[j])/max(1e-6,cum[j+1]-cum[j]); out.append([round(P[j][k]+(P[j+1][k]-P[j][k])*t,3) for k in range(3)]); s+=1.0
  return out
DECK=[[x,z,h+0.12] for x,z,h in deckSample(F110)]
DECK=resample(DECK)
A6=resample(json.load(open('/root/cap/m1/a6.json')))
HELP=("window.__PA={deck:%s,a6:%s};"%(json.dumps(DECK),json.dumps(A6)))+r"""
window.__at=(nm,s,dir,lane)=>{const P=window.__PA[nm];const g=i=>P[Math.max(0,Math.min(P.length-1,i))];const f=s,i=Math.floor(f),t=f-i;const a=g(i),b=g(i+1);
 let x=a[0]+(b[0]-a[0])*t,z=a[1]+(b[1]-a[1])*t,y=a[2]+(b[2]-a[2])*t;const p0=g(Math.round(s-4)),p1=g(Math.round(s+4));let dx=(p1[0]-p0[0])*dir,dz=(p1[1]-p0[1])*dir;const l=Math.hypot(dx,dz)||1;dx/=l;dz/=l;
 const rx=-dz,rz=dx; x+=rx*lane;z+=rz*lane; return {x,z,y,fx:dx,fz:dz,rx,rz,h:Math.atan2(dx,dz)};};
{const W9=window.__W();if(!window.__HID){window.__HID=1;W9.scene.traverse(o=>{if(o.userData&&o.userData.isCar){try{Object.defineProperty(o,'visible',{get(){return false},set(){}});}catch(e){}}});}
 if(!window.__GT){const g=W9.makeCar(W9.CARS.find(c=>c.id=='gt'));W9.scene.add(g);window.__GT=g;}window.__GT.visible=true;window.__lt=null;}
{const e=document.getElementById('screen');if(e){e.classList.add('hidden');e.innerHTML='';}}
"""
def car(nm,s0,v,dir,lane,ground=False):
  # place la GT et renvoie C (repère voiture)
  return ("const W7=window.__W();const g=window.__GT;const s=%f+%f*T*%d;const C=window.__at('%s',s,%d,%f);"%(s0,v,dir,nm,dir,lane)+
   ("C.y=W7.GH(C.x,C.z);const yf=W7.GH(C.x+C.fx*1.6,C.z+C.fz*1.6),yb=W7.GH(C.x-C.fx*1.6,C.z-C.fz*1.6);g.rotation.order='YXZ';g.rotation.x=-Math.atan2(yf-yb,3.2);" if ground else "")+
   "g.position.set(C.x,C.y,C.z);g.rotation.y=C.h;if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;"%v)
def cam(px,py,pz,tx,ty,tz,fov=62):
  return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(px,py,pz,tx,ty,tz,fov)
def rel(a,r,u):  # point relatif à la voiture : a devant, r à droite, u en haut
  return ("C.x+C.fx*(%s)+C.rx*(%s)"%(a,r),"C.y+(%s)"%u,"C.z+C.fz*(%s)+C.rz*(%s)"%(a,r))
# index du deck le plus proche d'un x
def sx(P,x): return min(range(len(P)),key=lambda i:abs(P[i][0]-x))
S={}
# A : F110 vers l'ouest, caméra basse derrière, faisceaux du stade devant
sA=sx(DECK,240)
S['A']=(96,car('deck',sA,30,-1,4.2)+cam(*rel("-6.8-0.35*T","1.7-0.6*T","1.2+0.1*T"),*rel("30","-1","2.6"),fov=60))
sB=sx(DECK,-140)
S['B']=(56,car('deck',sB,30,-1,4.2)+cam(*rel("-4+2.5*T","-16","5.5"),*rel("6","22","4"),fov=62))
iC=min(range(len(A6)),key=lambda i:abs(A6[i][1]-1035))
S['C']=(56,car('a6',iC,22,1,3.2,True)+cam(*rel("13-3*T","-0.9","1.0"),*rel("0","0","0.9"),fov=56))
iD=min(range(len(A6)),key=lambda i:abs(A6[i][1]-1080))
S['D']=(80,car('a6',iD,22,1,3.2,True)+cam(*rel("-16","-4","17"),*rel("18","0","1"),fov=62))
if __name__=="__main__":
  sel=sys.argv[1].split(','); mode=sys.argv[2]; dt=int(sys.argv[3]) if len(sys.argv)>3 else 840
  shots=[]
  for k in sel:
    n,b=S[k]
    if mode=='r':
      for t in (0.0,(n-1)/30*0.5,(n-1)/30): shots.append(shot("%s_t%02d"%(k,int(t*10)),b,dayT=dt,toff=t,wait=1500,js=notraf+HELP))
    else: shots.append(shot("de_"+k,b,dayT=dt,n=n,wait=2500,js=notraf+HELP))
  out='/root/cap/m1/'+('f' if mode=='f' else 'r')
  print(run(shots,out,w=1080 if mode=='f' else 540,h=960 if mode=='f' else 480,wait=True))
