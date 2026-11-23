# M3 Gratuit b1 (mer. 25/11 17h, DEUX ÉCRANS) · Constancy Sud de jour, vraies voitures garées (V310.30) et passants
DT=int(os.environ.get("DT","480"))
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
HB="{const W6=window.__W();if(!window.__HB){window.__HB=1;const H=o=>{if(o&&o.isObject3D)Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});};const B=W6.BANNER;if(B){H(B.g);H(B.plane);H(B.cloth);}W6.scene.traverse(o=>{if(o.isMesh&&o.material&&o.material.blending===2&&o.geometry){o.geometry.computeBoundingBox();const bb=o.geometry.boundingBox;if(o.scale.y*(bb.max.y-bb.min.y)>100)H(o);}});(W6.JW&&W6.JW.beams||[]).forEach(b=>H(b.isObject3D?b:(b.m||b.mesh)));}}"
UNFPV="{const W6=window.__W();W6.G.fpv=false;W6.G.mode='play';}"
def MK(name,body,n=1,o=0,js="",wait=2500):
  s=shot(name,body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+HB+UNFPV+js); s["far"]=20000; return s
S={}
S["TA"]=L(("160","140","900"),("160","0","899"),70)
S["TB"]=L(("680","140","1000"),("680","0","999"),70)
S["TC"]=L(("-680","140","1000"),("-680","0","999"),70)
