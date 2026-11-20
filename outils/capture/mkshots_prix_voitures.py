import json,sys
sys.path.insert(0,'/tmp/claude-0/-home-claude-constancy/30839bf3-cb44-59e2-b004-ce72188adf1a/scratchpad/gen2')
from jn import hide,fw
notraf="{const W8=window.__W();W8.traffic.forEach(a=>{if(a.mesh)a.mesh.visible=false;});}"
def place(cars):
  # cars: list of (id,x,z,h)
  s="{const W9=window.__W();window.__PC=window.__PC||[];window.__PC.forEach(g=>W9.scene.remove(g));window.__PC=[];"
  for cid,x,z,h in cars:
    s+="{const d=W9.CARS.find(c=>c.id=='%s');const g=W9.makeCar(d);g.position.set(%f,0,%f);g.rotation.y=%f;W9.scene.add(g);window.__PC.push(g);}"%(cid,x,z,h)
  return s+"}"
def cam(body,toff=0):
  return "(G)=>{const T=(performance.now()-(window.__T0||performance.now()))/1000+(%s);%s}"%(toff,body)
def shot(name,body,dayT,cars,n=1,toff=0,wait=2500):
  return {"name":name,"n":n,"wait":wait,"dayT":dayT,"js":hide+";"+fw+notraf+place(cars),"camjs":cam(body,toff)}
def job(path,out,shots,w,h): json.dump({"out":out,"w":w,"h":h,"shots":shots},open(path,'w'))
