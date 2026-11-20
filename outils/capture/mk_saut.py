import json,sys
sys.path.insert(0,'/home/claude/rushes/outils/capture')
import cl
hide,fw=cl.hide,cl.fw
def setup(x,z,h,alt,climb=1,side=0):
  return """
{const W7=window.__W(),g=W7.G;
 if(g.para){g.para=null;} W7.scene.traverse(o=>{if(o.userData&&o.userData.v2)o.visible=false;});
 if(g.ghost){g.ghost.mesh.position.set(0,-900,0);g.ghost=null;}
 g.autoJump=false; window.__ini=0; window.__TJ=null; window.__CS=null;
 window.__auto=(G)=>{ if(window.__T0==null) return {fwd:0,side:0,brake:false};
   if(!window.__ini && !G.onFoot){const c=G.car;c.x=%f;c.z=%f;c.h=%f;c.alt=%f;c.v=46;c.pitch=0.05;c.roll=0;c.toT=99;c.thin=3;window.__ini=1;}
   return {fwd:%f,side:%f,brake:false}; };
 if(g.onFoot && !g.para){ const r=W7.rentals.filter(q=>q.kind=='avion').sort((p,q)=>Math.hypot(p.x-175,p.z-512)-Math.hypot(q.x-175,q.z-512))[0]; g.me.x=r.x+3; g.me.z=r.z; g.me.h=0; W7.toggleCar(); }
}""" % (x,z,h,alt,climb,side)
def job(path,out,shots,w=540,h=960):
  json.dump({"out":out,"w":w,"h":h,"shots":shots},open(path,'w'))
def shot(name,n,dayT,js,camjs,wait=5000,pre=3):
  return {"name":name,"n":n,"wait":wait,"dayT":dayT,"js":hide+";"+fw+";"+js,"camjs":camjs,"far":6000,"pre":pre}
