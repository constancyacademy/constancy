# povparachute_b1 (jeu. 26/11 12h, M2 POV, COMMANDE de l'expert du 24/11 19h45) · « POV : Tu sautes au-dessus de ta ville. »
# Le VRAI saut du jeu : avion de location, placé en vol, W.toggleCar() en vol = startParachute (voile qui s'ouvre en 0,6 s), descente pilotée par window.__auto
import os,math
DT=int(os.environ.get("DT","420"))
def SETUP(x,z,h,alt,fwd=0.5,side=0.0,tj=0.05):
  return """{const W7=window.__W(),g=W7.G;g.mode='play';g.fpv=false;
 if(g.para){g.para=null;}
 if(g.ghost){try{g.ghost.mesh.position.set(0,-900,0);}catch(e){} g.ghost=null;}
 if(!g.onFoot){try{W7.toggleCar();}catch(e){} g.onFoot=true; g.ride={kind:'none'};}
 g.autoJump=false; window.__ini=0; window.__jumped=0;
 window.__auto=(G)=>{ if(window.__T0==null) return {fwd:0,side:0,brake:false};
   const T=(performance.now()-window.__T0)/1000;
   if(!window.__ini && !G.onFoot){const c=G.car;c.x=%f;c.z=%f;c.h=%f;c.alt=%f;c.v=46;c.pitch=0.0;c.roll=0;c.toT=99;c.thin=3;window.__ini=1;}
   if(window.__ini && !window.__jumped && !G.onFoot && T>%f){window.__jumped=1;W7.toggleCar();}
   if(G.para) return {fwd:%f,side:%f,brake:false};
   return {fwd:1,side:0,brake:false}; };
 const r=W7.rentals.filter(q=>q.kind=='avion').sort((p,q)=>Math.hypot(p.x-175,p.z-512)-Math.hypot(q.x-175,q.z-512))[0]; g.me.x=r.x+3; g.me.z=r.z; g.me.h=0; g.doorClose=null; W7.toggleCar();
}""" % (x,z,h,alt,tj,fwd,side)
# caméra : suit le perso (lissée), 3/4 avant au-dessus, regarde le perso et la ville en dessous
def CAM(a=2.2,d=9.0,hg=4.0,td=3.0,fov=62,k=0.35):
  return ("const W=window.__W(),g=W.G;let ax,ay,az,h;if(g.para){ax=g.me.x;ay=g.para.alt+1.2;az=g.me.z;h=g.me.h;}else{ax=g.car.x;ay=(g.car.alt||0);az=g.car.z;h=g.car.h;}"
    "let S=window.__CS;if(!S||Math.hypot(ax-S.x,ay-S.y,az-S.z)>40){S=window.__CS={x:ax,y:ay,z:az,h:h};}S.x+=(ax-S.x)*%f;S.y+=(ay-S.y)*%f;S.z+=(az-S.z)*%f;S.h+=(h-S.h)*%f;"
    "const a=%f,d=%f;return {p:[S.x-Math.sin(S.h+a)*d,S.y+(%f),S.z-Math.cos(S.h+a)*d],t:[S.x,S.y-(%f),S.z],fov:%f};")%(k,k,k,k,a,d,hg,td,fov)
def MKP(name,setup,cam,n=1,wait=4000):
  s=shot(name,cam,dayT=DT,n=n,toff=0,wait=wait,js=NO+NOPLANE+setup+";window.__CS=null;"); s["far"]=20000; s["pre"]=1; return s
PLAYSTEP="{const W6=window.__W();if(!window.__stepP){const s0=window.__step;window.__step=ms=>{W6.G.mode='play';return s0(ms);};window.__stepP=1;}}"
