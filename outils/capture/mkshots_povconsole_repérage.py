import sys,math; sys.path.insert(0,'/root/cap'); from h import *
sys.path.insert(0,'/home/claude/rushes/outils/capture')
CLOUD="{const W6=window.__W();if(!window.__NCL){window.__NCL=1;W6.scene.traverse(o=>{if(o.isInstancedMesh&&o.material&&o.material.uniforms&&o.material.uniforms.sheet){Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}}"
def place(cars):
  s="{const W9=window.__W();window.__PC=window.__PC||[];window.__PC.forEach(g=>W9.scene.remove(g));window.__PC=[];"
  for cid,x,z,h in cars:
    s+="{const d=W9.CARS.find(c=>c.id=='%s');const g=W9.makeCar(d);g.position.set(%f,0,%f);g.rotation.y=%f;W9.scene.add(g);window.__PC.push(g);}"%(cid,x,z,h)
  return s+"}"
LZ=171.6
def carjs(X0,V,Z,ry=math.pi/2):
  return "const W7=window.__W();const g=window.__PC[0];const cx=%f+%f*T;g.position.set(cx,Math.max(0,W7.GH(cx,%f)),%f);g.rotation.y=%f;if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;"%(X0,V,Z,Z,ry,V)
CAR=notraf+place([("gt",-100,LZ,math.pi/2)])+"window.__lt=null;"
FIX="{const g=window.__PC[0];g.traverse(o=>{if(o.isMesh&&o.material){const ms=Array.isArray(o.material)?o.material:[o.material];ms.forEach(m=>{if(m.envMap){m.envMap=null;m.needsUpdate=true;}if(m.specular)m.specular.setRGB(0.15,0.15,0.15);if(m.shininess>40)m.shininess=40;});}});}"
GRAB="{const W3=window.__W();if(!window.__HM){window.__HM=W3.life.heli.mesh;W3.life.heli.mesh=new THREE.Group();}}"
S={
# GT passes under/next to a low camera
"gt":(CAR+FIX,carjs(-90,26,LZ)+"const k=Math.min(1,T/2.0);const of=8-4*k;return {p:[cx+of,0.55,%f+3.1],t:[cx+0.6,0.8,%f],fov:52};"%(LZ,LZ)),
"heli":(GRAB,"const M=window.__HM;const hx=-60+38*T,hz=-10,hy=165;M.position.set(hx,hy,hz);M.rotation.set(0,Math.PI/2,0.08);return {p:[hx-26+6*T,hy+9,hz+24],t:[hx+6,hy-6,hz],fov:60};"),
"stade":("","return {p:[-175+90-25*T,48-4*T,985+60-8*T],t:[-175,8,985],fov:60};"),
"drone":("","return {p:[260-60*T,380,520-50*T],t:[0,0,-60-50*T],fov:62};"),
}
def mk(k,n=1,o=0,name=None,dt=360):
  pre,body=S[k]; s=shot(name or "%s_%02d"%(k,int(o*10)),body,dayT=dt,n=n,toff=o,wait=1500,js=CLOUD+open("/root/w/noufo.js").read()+pre); s["far"]=20000; return s
if __name__=="__main__" and len(sys.argv)>3:
  sel=sys.argv[1].split(','); offs=[float(v) for v in sys.argv[2].split(',')]; out=sys.argv[3]
  run([mk(k,o=o) for k in sel for o in offs],out)
  from PIL import Image
  import glob
  rows=[]
  for k in sel:
    fs=sorted(glob.glob(out+'/'+k+'_*.png')); rows.append([Image.open(f).resize((270,480)) for f in fs])
  Wd=max(len(r) for r in rows); I=Image.new('RGB',(270*Wd,480*len(rows)))
  for j,r in enumerate(rows):
    for i,im in enumerate(r): I.paste(im,(i*270,j*480))
  I.save(out+'.png')
