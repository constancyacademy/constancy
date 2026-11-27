exec(open('/root/w/vi/lib.py').read())
INT=("{const W9=window.__W();const E=W9.APTX.list.find(e=>e.a.id==='villa');if(!window.__VG){const a=W9.AGENCE.find(x=>x.id==='villa');const g=W9.buildApt(a);g.position.set(E.sp.x,E.sp.y,E.sp.z);g.rotation.y=E.sp.ry;W9.scene.add(g);g.updateMatrixWorld(true);window.__VG=g;}"
     "(E.hide||[]).forEach(m=>{if(!m.__h){m.__h=1;Object.defineProperty(m,'visible',{configurable:true,get:()=>!!window.__EXT,set:()=>{}});}});"
     "const hl=W9.homeLight();if(hl){const S=W9.APT_SPEC.villa;const lp=new THREE.Vector3(0,S.H-0.6,0).applyMatrix4(window.__VG.matrixWorld);hl.position.copy(lp);hl.distance=Math.max(S.W,S.D)*1.4;hl.intensity=%s;}window.__EXT=%s;}")
def MKI(name,body,n=1,o=0,hl=0.9,ext=0,js=""):
  return MK(name,body,n=n,o=o,js=js+INT%(hl,ext))
