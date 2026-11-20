import json,sys,math
hide=open('/home/claude/rushes/outils/capture/hide.js').read().strip()
fix="try{const W2=window.__W();Object.values(W2.beacons||{}).forEach(b=>{if(b)b.visible=false;});if(W2.destBeacon)W2.destBeacon.visible=false;if(W2.ownMark)W2.ownMark.visible=false;window.__FW&&window.__FW.pts&&(window.__FW.pts.visible=false);}catch(e){} const DK=window.__MAPB().DK; DK.cars.forEach((c,k)=>{ c.lane = (k%2? c.D.w*0.28 : 0.001); c.sp=1.0; });"
H="""const DK=window.__MAPB().DK;const L=(a,b,k)=>a.map((v,i)=>v+(b[i]-v)*k);const E=k=>k<0?0:k>1?1:(1-Math.pow(1-k,2));
const PS=(S,s)=>{let i=0;while(i<S.length-2&&S[i+1][3]<s)i++;const a=S[i],b=S[i+1],t=(s-a[3])/Math.max(1e-6,b[3]-a[3]);return [a[0]+(b[0]-a[0])*t,a[2]+(b[2]-a[2])*t,a[1]+(b[1]-a[1])*t];};
const NEAR=(S,X,Z)=>{let bi=0,bd=1e9;S.forEach((p,i)=>{const d=Math.hypot(p[0]-X,p[1]-Z);if(d<bd){bd=d;bi=i;}});return S[bi][3];};
const CARN=(nm,k,X,Z,lead)=>{const cs=DK.cars.filter(c=>c.D.name.startsWith(nm));const c=cs[k%cs.length],S=c.D.S,Lt=S[S.length-1][3];if(window.__T0==null){c.sp=1.0;c.u=((NEAR(S,X,Z)-lead)/Lt+1)%1;}return {c,S,Lt,s:c.u*Lt};};
const NX=695,NZ=258;const PLACE=()=>{CARN('Constancy Express',0,NX,NZ,22);CARN('Constancy Express',1,NX,NZ,55);CARN('Constancy Express',2,NX,NZ,-8);CARN('Viaduc',0,NX,NZ,12);CARN('Viaduc',1,NX,NZ,46);CARN('Viaduc',2,NX,NZ,-20);};PLACE();"""
def camjs(body,toff=0):
  return "(G)=>{const T=(performance.now()-(window.__T0||performance.now()))/1000+%s;%s%s}"%(toff,H,body)
def orbit(R,Hh,th0,w,ty=20,fov=60,cx=695,cz=258):
  return "const th=%f+%f*T;return {p:[%f+%f*Math.cos(th),%f,%f+%f*Math.sin(th)],t:[%f,%f,%f],fov:%f};"%(th0,w,cx,R,Hh,cz,R,cx,ty,cz,fov)
SH={}
for i,(R,Hh,th0) in enumerate([(60,42,math.pi/4),(60,42,5*math.pi/4),(60,42,3*math.pi/4),(60,42,-math.pi/4),(48,34,math.pi/4),(48,34,5*math.pi/4),(75,55,3*math.pi/4),(75,55,-math.pi/4)]):
  SH["O%d"%i]=orbit(R,Hh,th0,0.6)
for i,(R,Hh,th0,cx,cz) in enumerate([(280,170,math.pi/4,650,230),(320,190,0.2,650,230),(300,180,math.pi/2+0.3,650,230),(260,150,-math.pi/4,650,230)]):
  SH["W%d"%i]="const th=%f+0.1*T;return {p:[%f+%f*Math.cos(th),%f,%f+%f*Math.sin(th)],t:[%f,0,%f],fov:62};"%(th0,cx,R,Hh,cz,R,cx,cz)
SH2={}
import math as _m
th0=5*_m.pi/4-0.95
SH2["O"]="const th=%f+1.5*T;return {p:[695+46*Math.cos(th),42,258+46*Math.sin(th)],t:[695,18,258],fov:62};"%(5*_m.pi/4-0.75)
SH2["R"]="const o=CARN('Viaduc',1,NX,NZ,46);const s=o.c.u*o.Lt;const p=PS(o.S,s),q=PS(o.S,s+6);const dx=(q[0]-p[0])/6,dz=(q[2]-p[2])/6;const k=E(T/1.1);const bk=12-4*k;return {p:[p[0]-dx*bk,p[1]+4.5+30*k,p[2]-dz*bk],t:[p[0]+dx*(16+22*k),p[1]+1.5-14*k,p[2]+dz*(16+22*k)],fov:66};"
SH2["W"]="const th=0.12+0.35*T,RR=300-30*T;return {p:[650+RR*Math.cos(th),210-12*T,230+RR*Math.sin(th)],t:[530,0,215],fov:62};"
mode=sys.argv[1]; dt=int(sys.argv[2]); out=sys.argv[3]
shots=[]
if mode=="scout":
  for n,b in SH.items():
    shots.append({"name":n,"n":1,"wait":2500,"dayT":dt,"js":hide+fix,"camjs":camjs(b)})
  w,h=540,960
elif mode=="scout2":
  for n,toffs in (("R",(0,0.5,1.0)),("W",(0,)),("O",(0.5,1.4))):
    for t in toffs: shots.append({"name":"%s%d"%(n,int(t*10)),"n":1,"wait":2500,"dayT":dt,"js":hide+fix,"camjs":camjs(SH2[n],t)})
  w,h=540,960
else:
  for n,nf in (("O",45),):
    shots.append({"name":n,"n":nf,"wait":3000,"dayT":dt,"js":hide+fix,"camjs":camjs(SH2[n])})
  w,h=1080,1920
json.dump({"out":out,"w":w,"h":h,"shots":shots},open(sys.argv[4],'w'))
