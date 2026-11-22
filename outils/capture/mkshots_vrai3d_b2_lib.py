import sys,math; sys.path.insert(0,'/home/claude/rushes/outils/capture')
exec(open('/home/claude/rushes/outils/capture/mkshots_povconsole_repérage.py').read().split('S={')[0])
HIDECARS="{const W9=window.__W();W9.scene.traverse(o=>{if(o.userData&&o.userData.isCar&&!(window.__PC||[]).includes(o)&&!o.__hid){o.__hid=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}"
NO=CLOUD+open("/root/w/noufo.js").read()+"{if(window.__HM)window.__HM.visible=false;}"
LZ4=4.0; X0=60.0
PRE=notraf+place([("minuit",X0,LZ4,math.pi/2)])+"window.__lt=null;"+HIDECARS
def orbit(a0,a1,dur,r=6.8,h=2.0,ty=0.25,fov=55):
  return "const g=window.__PC[0];g.position.set(%f,Math.max(0,window.__W().GH(%f,%f)),%f);g.rotation.y=Math.PI/2;const k=Math.min(1,T/%f);const a=%f+(%f)*k;return {p:[%f+%f*Math.cos(a),%f,%f+%f*Math.sin(a)],t:[%f,%f,%f],fov:%d};"%(X0,X0,LZ4,LZ4,dur,a0,a1-a0,X0,r,h,LZ4,r,X0,ty,LZ4,fov)
def S_(name,b,n,dt=840,toff=0,wait=4000,pre=PRE):
  s=shot(name,b,dayT=dt,n=n,toff=toff,wait=wait,js=NO+pre); s["far"]=20000; return s
HIDELIGHTS="{const W9=window.__W();let n=0;W9.scene.traverse(o=>{if(o.isPoints&&o.frustumCulled===false&&o.material&&Math.abs(o.material.size-2.6)<1e-6)n=o.geometry.attributes.position.count;});if(n)W9.scene.traverse(o=>{if(o.isPoints&&o.geometry.attributes.position.count===n&&!o.__h){o.__h=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});window.__NL=n;}"
def place2(x):
  return notraf+place([("minuit",x,LZ4,math.pi/2)])+"window.__lt=null;"+HIDECARS+HIDELIGHTS
def orbit2(x,a0,a1,dur,r=6.8,h=1.1,ty=0.55,fov=55):
  return "const g=window.__PC[0];g.position.set(%f,Math.max(0,window.__W().GH(%f,%f)),%f);g.rotation.y=Math.PI/2;const k=Math.min(1,T/%f);const a=%f+(%f)*k;return {p:[%f+%f*Math.cos(a),%f,%f+%f*Math.sin(a)],t:[%f,%f,%f],fov:%d};"%(x,x,LZ4,LZ4,dur,a0,a1-a0,x,r,h,LZ4,r,x,ty,LZ4,fov)
