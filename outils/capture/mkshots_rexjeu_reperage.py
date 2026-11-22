import sys,math; sys.path.insert(0,'/root/cap'); from h import *
CLOUD="{const W6=window.__W();if(!window.__NCL){window.__NCL=1;W6.scene.traverse(o=>{if(o.isInstancedMesh&&o.material&&o.material.uniforms&&o.material.uniforms.sheet){Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}}"
PRE="const W6=window.__W();const g=W6.REX.d.g;const P=g.position;const hh=g.rotation.y;const fx=Math.sin(hh),fz=Math.cos(hh),sx=Math.cos(hh),sz=-Math.sin(hh);const HT=window.__RHT||(window.__RHT=(()=>{const b=new THREE.Box3().setFromObject(g);return b.max.y-b.min.y;})());"
def rel(f,s,u,tf,ts,tu,fov=55):
  return "return {p:[P.x+fx*(%s)+sx*(%s),P.y+(%s),P.z+fz*(%s)+sz*(%s)],t:[P.x+fx*(%s)+sx*(%s),P.y+(%s),P.z+fz*(%s)+sz*(%s)],fov:%s};"%(f,s,u,f,s,tf,ts,tu,tf,ts,fov)
S={
"far1":rel("200","120","6","0","0","45",60),
"far2":rel("0","260","6","0","0","45",60),
"q5":rel("70","40","25","0","0","24",50),
"q6":rel("70","40","12","0","0","26",52),
"rise":rel("62","30","3+16*T","0","0","8+16*T",54),
"prof":rel("0","85","18","0","0","18",52),
"q1":rel("95","60","45","0","0","30"),
"q2":rel("95","-60","45","0","0","30"),
"q3":rel("120","45","70","0","0","25"),
"q4":rel("20","120","40","0","0","30"),
}
def mk(k,n=1,o=0,name=None,dt=840):
  s=shot(name or "%s_%02d"%(k,int(o*10)),S[k],dayT=dt,n=n,toff=o,wait=2500,js=CLOUD+open("/root/w/noufo.js").read()+open("/root/w/rexfix.js").read(),pre=PRE); s["far"]=20000; return s
if __name__=="__main__" and len(sys.argv)>3:
  sel=sys.argv[1].split(','); offs=[float(v) for v in sys.argv[2].split(',')]; out=sys.argv[3]
  print(run([mk(k,o=o) for k in sel for o in offs],out,ev="(()=>{const W=window.__W();const g=W.REX.d&&W.REX.d.g;if(!g)return 'nog';const b=new THREE.Box3().setFromObject(g);return {p:g.position.toArray(),ry:g.rotation.y,min:b.min.toArray(),max:b.max.toArray(),ch:g.children.length}})()"))
  from PIL import Image
  import glob
  fs=sorted(glob.glob(out+'/*.png')); ims=[Image.open(f).resize((270,480)) for f in fs]
  I=Image.new('RGB',(270*len(ims),480))
  for i,im in enumerate(ims): I.paste(im,(i*270,0))
  I.save(out+'.png')
