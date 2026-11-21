import json,os,time,sys
hide=open('/root/cap/hide.js').read().strip()
fw="const W5=window.__W();window.__FW&&window.__FW.pts&&(window.__FW.pts.visible=false);W5.scene.traverse(o=>{const m=o.material;if(m&&m.uniforms&&m.uniforms.uK)m.visible=false;});try{Object.values(W5.beacons||{}).forEach(b=>{if(b)b.visible=false;});if(W5.destBeacon)W5.destBeacon.visible=false;if(W5.ownMark)W5.ownMark.visible=false;}catch(e){}"
notraf="{const W8=window.__W();W8.traffic.forEach(a=>{if(a.mesh)a.mesh.visible=false;});}"
def cam(body,toff=0,pre=""):
  return "(G)=>{const T=(performance.now()-(window.__T0||performance.now()))/1000+(%s);%s%s}"%(toff,pre,body)
def shot(name,body,dayT=840,n=1,toff=0,wait=2500,js="",rain=0,pre=""):
  return {"name":name,"n":n,"wait":wait,"dayT":dayT,"rain":rain,"js":hide+";"+fw+js,"camjs":cam(body,toff,pre)}
def look(p,t,fov=60):
  return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
_c=[0]
def run(shots,out,w=540,h=960,ev=None,wait=True,name=None):
  _c[0]+=1; nm=name or "j%d_%d"%(int(time.time()),_c[0])
  d={"out":out,"w":w,"h":h,"shots":shots}
  if ev: d["eval"]=ev
  p="/root/cap/jobs/%s.json"%nm; json.dump(d,open(p+".tmp",'w')); os.rename(p+".tmp",p)
  if not wait: return p
  while not os.path.exists(p+".done"): time.sleep(2)
  if os.path.exists(p+".err"): print("ERR",open(p+".err").read()[:2000])
  if os.path.exists(p+".res"): return json.load(open(p+".res"))
  return p
def montage(out,names,cols=4,scale=270):
  import glob,subprocess
  fs=[]
  for n in names: fs+=sorted(glob.glob(out+"/"+n+"_*.png"))
  return fs
