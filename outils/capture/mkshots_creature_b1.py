import sys
sys.path.insert(0,'/root/cap'); sys.path.insert(0,'/home/claude/rushes/outils/capture')
exec(open('/root/cap/rex.py').read())
exec(open('/home/claude/rushes/outils/capture/mkshots_rexvf_b2.py').read().split('SH={')[0].replace('from rex import *',''))
DT=840
NEAR=""
def MK(name,body,n=1,o=0,js="",wait=2500): return mk(name,body,n=n,o=o,dt=DT,js=js,wait=wait)
S={}
# P1 : dehors, à travers les baies, Rex qui marche, tube néon rose en haut du mur
S["I1"]=camA(1.0,0.80,"66-1.0*T",3,"Head",0.5,0.40,64)
S["I2"]=camA(1.0,0.55,"64-1.0*T",2,"Head",0.45,0.42,66)
S["I3"]=camA(1.0,0.30,"68-1.0*T",5,"EYES",0.5,0.45,60)
# P4 : arc du profil à la face, Rex entier
S["F1"]=camR(1.6,"44*Math.sin(0.15+0.5*T)","-44*Math.cos(0.15+0.5*T)","4","L_Foot",0.5,0.72,80)
S["F2"]=camR(1.6,"40*Math.sin(0.5+0.45*T)","-40*Math.cos(0.5+0.45*T)","3","L_Foot",0.5,0.74,82)
# P2 : perso qui longe le mur vers le Rex, vu de 3/4 face
def WALK(a0,db,rr,fwd=0.1):
  return ("{const W6=window.__W(),G=W6.G,d=W6.REX.d;G.mode='play';G.fpv=false;if(!G.onFoot){G.car.v=0;G.entering=null;G.wantExit=false;W6.toggleCar();}G.doorClose=null;G.entering=null;"
          "const b=(%s)+(%s);G.me.x=d.cx+Math.cos(b)*(%s);G.me.z=d.cz+Math.sin(b)*(%s);G.me.v=0;G.me.h=Math.atan2(Math.sin(b),-Math.cos(b));W6.meMesh.visible=true;"
          "window.__auto=(g)=>{if(window.__T0==null)return {fwd:0,side:0};return {fwd:%s,side:0};};}")%(a0,db,rr,rr,fwd)
def WCAM(a0,db,ahead,out,h,back,up,fov):
  return (PIN(a0)+"const G7=W6.G,me=G7.me,b=(%s)+(%s),tx=Math.sin(b),tz=-Math.cos(b),nx=Math.cos(b),nz=Math.sin(b),my=W6.GH(me.x,me.z);"
          "return {p:[me.x+tx*(%s)+nx*(%s),my+(%s),me.z+tz*(%s)+nz*(%s)],t:[me.x-tx*(%s),my+(%s),me.z-tz*(%s)],fov:%s};")%(a0,db,ahead,out,h,ahead,out,back,up,back,fov)
WJ={}
for k,(db,ah,ou,h,bk,up,fov) in {"W1":(0.38,5.5,2.2,1.6,10,5,62),"W2":(0.42,4.5,3.0,1.3,14,7,66),"W3":(0.32,6.0,1.2,1.8,12,6,60)}.items():
  S[k]=WCAM(1.0,db,ah,ou,h,bk,up,fov); WJ[k]=WALK(1.0,db,58)
_MK=MK
def MK(name,body,n=1,o=0,js="",wait=2500):
  k=[x for x in WJ if S[x]==body]
  return _MK(name,body,n=n,o=o,js=js+(WJ[k[0]] if k else ""),wait=wait)
def WCAM2(a0,db,ahead,out,h,k,up,fov):
  return (PIN(a0)+"const G7=W6.G,me=G7.me,b=(%s)+(%s),tx=-Math.sin(b),tz=Math.cos(b),nx=Math.cos(b),nz=Math.sin(b),my=W6.GH(me.x,me.z);"
          "return {p:[me.x+tx*(%s)+nx*(%s),my+(%s),me.z+tz*(%s)+nz*(%s)],t:[me.x+(P.x-me.x)*(%s),my+(%s),me.z+(P.z-me.z)*(%s)],fov:%s};")%(a0,db,ahead,out,h,ahead,out,k,up,k,fov)
def WALK2(a0,db,rr,fwd=0.1):
  return WALK(a0,db,rr,fwd).replace("G.me.h=Math.atan2(Math.sin(b),-Math.cos(b))","G.me.h=Math.atan2(-Math.sin(b),Math.cos(b))")
for k,(db,ah,ou,h,kk,up,fov) in {"V1":(0.0,2.5,7,1.5,0.25,4.5,68),"V2":(-0.05,2.0,6,1.3,0.25,5,70),"V3":(0.0,3.0,8,1.7,0.3,4,64)}.items():
  S[k]=WCAM2(1.0,db,ah,ou,h,kk,up,fov); WJ[k]=WALK2(1.0,db,57.5)
for k,(db,ah,ou,h,kk,up,fov) in {"V4":(-0.04,3.5,5,1.4,0.22,4.2,62),"V5":(-0.06,3.0,4.5,1.2,0.25,4.5,64)}.items():
  S[k]=WCAM2(1.0,db,ah,ou,h,kk,up,fov); WJ[k]=WALK2(1.0,db,57.5)
S["I4"]=camA(1.0,0.62,"64-1.2*T",2,"Head",0.40,0.42,66)
S["I5"]=camA(1.0,0.50,"63-1.2*T",2.5,"EYES",0.42,0.44,64)
S["G1"]=camR(1.3,"40","-16","1.2+7*T","EYES",0.5,0.50,60)
S["G2"]=camR(1.3,"34","-12","1.0+6*T","EYES",0.45,0.46,64)
for k,(db,ah,ou,h,kk,up,fov) in {"V6":(-0.03,2.2,5.5,1.4,0.18,3.6,58),"V7":(0.0,2.0,4.5,1.3,0.15,3.2,60)}.items():
  S[k]=WCAM2(1.0,db,ah,ou,h,kk,up,fov); WJ[k]=WALK2(1.0,db,57.5)
NOAURA="try{const W6=window.__W();const A=W6.AURA||window.AURA;if(A&&A.ring&&!A.ring.__h){A.ring.__h=1;Object.defineProperty(A.ring,'visible',{configurable:true,get:()=>false,set:()=>{}});}}catch(e){}"
AWAY="{const W6=window.__W(),G=W6.G,d=W6.REX.d;G.mode='play';if(G.onFoot){G.me.x=d.cx+420;G.me.z=d.cz+60;G.me.v=0;}window.__auto=(g)=>({fwd:0,side:0});}"
S["F3"]=camR(1.6,"40*Math.sin(0.3+0.5*T)","-40*Math.cos(0.3+0.5*T)","3","L_Foot",0.5,0.74,82)
def MK(name,body,n=1,o=0,js="",wait=2500):
  k=[x for x in WJ if S[x]==body]
  return _MK(name,body,n=n,o=o,js=js+NOAURA+(WJ[k[0]] if k else AWAY),wait=wait)
S["V8"]=WCAM2(0.88,-0.03,2.2,5.5,1.4,0.18,3.6,58); WJ["V8"]=WALK2(0.88,-0.03,57.5)
S["F4"]=camR(1.6,"40*Math.sin(0.3+0.5*T)","-40*Math.cos(0.3+0.5*T)","3","L_Foot",0.5,0.80,88)
