from ufo import *
import math
ARR=7.2
dx,dz=10-X,28-Z; L=math.hypot(dx,dz); ux,uz=dx/L,dz/L
CLOUD="if(!window.__NCL){window.__NCL=1;W6.scene.traverse(o=>{if(o.isInstancedMesh&&o.material&&o.material.uniforms&&o.material.uniforms.sheet){Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}"
S={
"Bpre":(4.4,"const a=2.25+0.30*(T-0.5);return {p:[%f+62*Math.cos(a),7+3*(T-0.5),%f+62*Math.sin(a)],t:[%f,17+1.5*(T-0.5),%f],fov:58};"%(X,Z,X,Z)),
"A2":(1.5,"return {p:[%f-10*T,4.5+1.0*T,%f+2*T],t:[%f-3*T,16+6*T,%f],fov:58};"%(X-38,Z+38,X+6,Z-6)),
"C2":(ARR+28.6,"const ux=%f,uz=%f,a=-0.5-0.35*T;const sx=Math.cos(a)*uz-Math.sin(a)*ux,sz=-Math.cos(a)*ux-Math.sin(a)*uz;return {p:[M6.x+sx*15,M6.y+9,M6.z+sz*15],t:[M6.x-sx*4,M6.y+0.5,M6.z-sz*4],fov:60};"%(ux,uz)),
"A":(1.3,"return {p:[%f-9*T,4.5+1.2*T,%f+3*T],t:[M6.x,M6.y+11,M6.z],fov:60};"%(X-24,Z+34)),
"B":(4.9,"const a=2.25+0.30*T;return {p:[%f+62*Math.cos(a),7+3*T,%f+62*Math.sin(a)],t:[%f,17+1.5*T,%f],fov:58};"%(X,Z,X,Z)),
"C":(ARR+28.6,"const ux=%f,uz=%f,a=-0.5+0.35*T;const sx=Math.cos(a)*uz-Math.sin(a)*ux,sz=-Math.cos(a)*ux-Math.sin(a)*uz;return {p:[M6.x+sx*15,M6.y+9,M6.z+sz*15],t:[M6.x-sx*4,M6.y-5,M6.z-sz*4],fov:60};"%(ux,uz)),
"D":(ARR+33.0,"return {p:[M6.x+34-4*T,M6.y+46,M6.z+30-3*T],t:[M6.x,M6.y-27,M6.z],fov:62};"),
"E":(ARR+30.9,"const a=1.9+0.42*T;return {p:[M6.x+30*Math.cos(a),M6.y+16,M6.z+30*Math.sin(a)],t:[M6.x,M6.y-9,M6.z],fov:62};"),
}
def mk(k,o,n=1,name=None):
  t0,body=S[k]; s=shot(name or "%s_%02d"%(k,int(o*10)),body,dayT=840,n=n,wait=1200,js=setup(t0+o),pre=PRE+CLOUD); s["far"]=20000; return s
if __name__=="__main__":
  sel=sys.argv[1].split(','); offs=[float(v) for v in sys.argv[2].split(',')]
  out=sys.argv[3]
  shots=[mk(k,o) for k in sel for o in offs]
  run(shots,out)
  from PIL import Image
  import glob
  rows=[]
  for k in sel:
    fs=sorted(glob.glob(out+'/'+k+'_*.png')); rows.append([Image.open(f).resize((270,480)) for f in fs])
  Wd=max(len(r) for r in rows); I=Image.new('RGB',(270*Wd,480*len(rows)))
  for j,r in enumerate(rows):
    for i,im in enumerate(r): I.paste(im,(i*270,j*480))
  I.save(out+'.png')
