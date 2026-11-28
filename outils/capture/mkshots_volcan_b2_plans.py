exec(open('/root/w/v2/base.py').read())
import math
def CR(a,r0,dr,h0,dh,sh,ty,fov):
  c,s=math.cos(math.radians(a)),math.sin(math.radians(a))
  rx,rz=s,-c
  return L(V("(%f)*((%f)-(%f)*T)"%(c,r0,dr),"(%f)-(%f)*T"%(h0,dh),"(%f)*((%f)-(%f)*T)"%(s,r0,dr)),V(rx*sh,ty,rz*sh),fov)
# P1 image 1 : crater glow + gerbes, plume out on the left
S["P1"]=CR(78,64,12,194,8,14,130,60)
S["P1b"]=CR(72,64,12,194,8,15,130,60)
# P2 whole volcano, drone orbit
def ORB(a0,da,r,dr,h,ty,fov):
  return ("const a=(%f+(%f)*T)*Math.PI/180,rr=%f-(%f)*T;"%(a0,da,r,dr))+L(V("rr*Math.cos(a)",h,"rr*Math.sin(a)"),V(0,ty,0),fov)
S["P2"]=ORB(28,9,250,12,62,98,46)
S["P2b"]=ORB(-30,9,250,12,62,98,46)
# P3 bomb into the sea, close, volcano behind
def BOMB(a,R,tim,back,lat,ch,fov):
  c,s=math.cos(math.radians(a)),math.sin(math.radians(a))
  ix,iz=VX+c*R,VZ+s*R
  js=("{const W8=window.__W();const VO=W8.VOL;if(window.__T0!=null&&!window.__BK){window.__BK=1;const q=VO.bomb[0];const tf=6.0,tau=tf-%f-(T>0?T:0);const c=%f,s=%f;"
      "const L0=new THREE.Vector3(c*4,VO.top,s*4);const vh=(%f-4)/tf,vy0=(15*tf*tf-VO.top)/tf;q.life=9;q.sl=0;q.st.visible=false;q.s.visible=true;"
      "q.p=new THREE.Vector3(L0.x+c*vh*tau,VO.top+vy0*tau-15*tau*tau,L0.z+s*vh*tau);q.v=new THREE.Vector3(c*vh,vy0-30*tau,s*vh);}}")%(tim,c,s,R)
  cx,cz=ix+c*back-s*lat, iz+s*back+c*lat
  return js+"return {p:[%f-(%f)*T,%f,%f-(%f)*T],t:[%f,%f,%f],fov:%f};"%(cx,c*2,ch,cz,s*2,ix,10,iz,fov)
S["P3"]=BOMB(20,200,0.45,34,10,4,58)
# P4 player on the beach walking toward the sea, island glowing in front
S["P4"]=CAMP+"return {p:[me.x-fx*7+rx*3,my+2.0,me.z-fz*7+rz*3],t:[me.x+fx*60,my+30,me.z+fz*60],fov:56};"; PL["P4"]=MEW(14,172)
# P5 POV photo
S["P5"]=("const u=Math.min(T,1.4),d=2.2*u;const sx=12-0.1*d,sz=163-0.99*d;"+L(V("sx","1.7","sz"),V(0,"95+3*T",0),50)); PL["P5"]=ME(12,166)
# P6 drone pulls back and rises over the player
S["P6"]=CAMP+"const b=6+7*T,h=2.5+5*T;return {p:[me.x-fx*b+rx*2,my+h,me.z-fz*b+rz*2],t:[me.x+fx*80,my+38+2*T,me.z+fz*80],fov:56};"; PL["P6"]=ME(8,165)
for k in list(S): 
  if k.startswith("P3"): PL[k]=PL.get(k,"")+"window.__BK=null;"
NORING="{const W6=window.__W();W6.scene.traverse(o=>{if(o.isMesh&&o.geometry&&o.geometry.type==='RingGeometry'&&o.geometry.parameters&&Math.abs(o.geometry.parameters.innerRadius-0.8)<1e-6&&!o.__h){o.__h=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}"
S["P4"]=CAMP+"return {p:[me.x+rx*7-fx*5,my+1.8,me.z+rz*7-fz*5],t:[me.x+fx*60-rx*6,my+14,me.z+fz*60-rz*6],fov:62};"; PL["P4"]=NORING+MEW(10,168)
S["P6"]=CAMP+"const b=5+6*T,h=2.2+4.5*T;return {p:[me.x-fx*b+rx*5,my+h,me.z-fz*b+rz*5],t:[me.x+fx*80,my+20+2*T,me.z+fz*80],fov:62};"; PL["P6"]=NORING+ME(16,164)
PL["P5"]=NORING+PL["P5"]
S["P3"]=BOMB(20,200,0.55,24,8,3,62)
PL["P3"]="window.__BK=null;"
S["P4"]=CAMP+"return {p:[me.x-fx*6+rx*4,my+1.8,me.z-fz*6+rz*4],t:[me.x+fx*60-rx*6,my+14,me.z+fz*60-rz*6],fov:62};"; PL["P4"]=NORING+ME(30,166)
S["P5"]=("const u=Math.min(T,1.6),d=2.0*u;const sx=31-0.18*d,sz=163-0.98*d;"+L(V("sx","1.7","sz"),V(0,"95+3*T",0),50)); PL["P5"]=NORING+ME(30,167)
S["P6"]=ORB(150,-7,205,40,"(32+20*T)",96,48)
S["X"]=L(V(0,300,300),V(0,0,0),60)
S["P4"]=CAMP+"return {p:[me.x-fx*7+rx*2.5,my+1.8,me.z-fz*7+rz*2.5],t:[me.x+fx*60-rx*6.9,my+14,me.z+fz*60-rz*6.9],fov:62};"; PL["P4"]=NORING+ME(30,166)
S["Q1"]=ORB(225,7,205,40,"(32+20*T)",96,48)
S["Q2"]=ORB(245,7,205,40,"(32+20*T)",96,48)
S["Q3"]=ORB(45,9,250,12,62,98,46)
S["P4"]=CAMP+"return {p:[me.x-fx*7+rx*2.0,my+1.8,me.z-fz*7+rz*2.0],t:[me.x+fx*60-rx*11,my+14,me.z+fz*60-rz*11],fov:62};"; PL["P4"]=NORING+ME(30,166)
S["P6"]=ORB(70,6,150,12,"(112+6*T)",150,52)
S["P6"]=CR(88,56,10,215,8,16,128,64)
