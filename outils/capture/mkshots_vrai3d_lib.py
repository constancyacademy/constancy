import sys,math; sys.path.insert(0,'/home/claude/rushes/outils/capture')
exec(open('/home/claude/rushes/outils/capture/mkshots_povconsole_repérage.py').read().split('S={')[0])
NO=CLOUD+open("/root/w/noufo.js").read()+"{if(window.__HM)window.__HM.visible=false;}"
LZ4=4.0; X0=60.0
PRE=notraf+place([("minuit",X0,LZ4,math.pi/2)])+"window.__lt=null;"
# orbit around parked car: angle a from a0 to a1 over dur
def orbit(a0,a1,dur,r=6.8,h=1.3):
  return "const g=window.__PC[0];g.position.set(%f,Math.max(0,window.__W().GH(%f,%f)),%f);g.rotation.y=Math.PI/2;const k=Math.min(1,T/%f);const e=k;const a=%f+(%f)*e;return {p:[%f+%f*Math.cos(a),%f,%f+%f*Math.sin(a)],t:[%f,0.75,%f],fov:55};"%(X0,X0,LZ4,LZ4,dur,a0,a1-a0,X0,r,h,LZ4,r,X0,LZ4)
def drive(V,body):
  return carjs(X0,V,LZ4)+body
def S_(name,b,n,dt=840,toff=0,wait=4000,pre=PRE):
  s=shot(name,b,dayT=dt,n=n,toff=toff,wait=wait,js=NO+pre); s["far"]=20000; return s
