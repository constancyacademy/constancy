import sys; sys.path.insert(0,'/root/cap')
from h import *
LX=395.6
CAR="{const W9=window.__W();if(window.__CC&&!window.__CC.__v2){W9.scene.remove(window.__CC);window.__CC=null;}if(!window.__CC){const d=W9.CARS.find(c=>c.id=='nacre');const g=W9.makeCar(d);if(g.userData.nacre){g.userData.nacre.em=[];}W9.scene.add(g);g.__v2=1;window.__CC=g;}window.__CC.visible=true;window.__lt=null;}"
# depthTest sur les traînées + faisceaux cachés
FIX=""
def carjs(Z0,V,fix=FIX):
  return "const W7=window.__W();const g=window.__CC;const cz=%f-%f*T;g.position.set(%f,0,cz);g.rotation.y=Math.PI;if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;%s"%(Z0,V,LX,V,fix)
PAN="{const W9=window.__W();W9.P.cash=5000;W9.openShop();const e=document.getElementById('screen');[e,...e.querySelectorAll('*')].forEach(x=>x.style.setProperty('visibility','visible','important'));const im=[...e.querySelectorAll('img')].find(x=>x.alt=='Constancy City');if(im&&!window.__SNP){try{const r=new THREE.WebGLRenderer({antialias:true,alpha:true,preserveDrawingBuffer:true});r.setSize(220,140);r.setClearColor(0,0);const sc=new THREE.Scene();sc.add(new THREE.HemisphereLight(0xffffff,0x444455,0.95));const dl=new THREE.DirectionalLight(0xffffff,0.7);dl.position.set(3,5,6);sc.add(dl);const cm=new THREE.PerspectiveCamera(35,220/140,0.1,100);const o=W9.makeCar(W9.CARS.find(c=>c.id=='nacre'));o.traverse(q=>{if(q.isSprite||(q.material&&q.material.blending===2&&q.geometry&&q.geometry.boundingSphere&&0))q.visible=false;});sc.add(o);o.updateMatrixWorld(true);const rr=4.7*0.75,cx=0,cy=0.7,cz=0;cm.position.set(cx+rr*1.1,cy+rr*0.45,cz+rr*1.6);cm.lookAt(cx,cy,cz);r.render(sc,cm);window.__SNP=r.domElement.toDataURL('image/png');sc.remove(o);}catch(er){window.__SNP='';}}if(im&&window.__SNP)im.src=window.__SNP;const p=e.querySelector('.panel');if(p&&window.innerWidth>900){p.style.zoom=window.__PZ||1.9;}setTimeout(()=>{if(p)p.scrollTop=99999;},30);}"
NOPAN="{const e=document.getElementById('screen');if(e){e.classList.add('hidden');e.innerHTML='';}}"
S={
"prep":(1,carjs(300,30)+"return {p:[%f,3,cz-9],t:[%f,0.7,cz],fov:50};"%(LX,LX)),
"f3q":(62,carjs(300,30)+"return {p:[%f+2.9,1.15,cz-7.0-0.5*T],t:[%f-0.1,0.65,cz+0.4],fov:52};"%(LX,LX)),
"f3qm":(62,carjs(300,30)+"return {p:[%f-3.0,1.2,cz-7.2-0.5*T],t:[%f+0.1,0.65,cz+0.4],fov:52};"%(LX,LX)),
"gagne":(43,carjs(260,30)+"const pp=document.querySelector('#screen .panel');if(pp){const k=Math.min(1,T/1.35),e2=k*k*(3-2*k);pp.style.transformOrigin='50%% 80%%';pp.style.transform='translateY('+(-330*e2)+'px) scale('+(1+0.22*e2)+')';}return {p:[%f+9-3*T,3.2,cz-9+2*T],t:[%f,0.8,cz],fov:55};"%(LX,LX)),
"profil":(36,carjs(250,30)+"return {p:[%f-6.8,0.9,cz-1.0],t:[%f,0.6,cz-1.0],fov:48};"%(LX,LX)),
"arriere":(43,carjs(280,30)+"return {p:[%f-1.6,2.4,cz+9.5],t:[%f,0.7,cz-1],fov:56};"%(LX,LX)),
"drone":(62,carjs(320,30)+"return {p:[%f+14,16,cz+18],t:[%f,0.5,cz-6],fov:60};"%(LX,LX)),
}
if __name__=="__main__":
  sel=sys.argv[1].split(','); mode=sys.argv[2]; dt=630
  shots=[]
  for k in sel:
    n,b=S[k]
    if mode=='r':
      for t in (0.3,(n-1)/30): shots.append(shot("%s_t%02d"%(k,int(t*10)),b,dayT=dt,toff=t,wait=1500,js=notraf+CAR+(PAN if k in('gagne',) else NOPAN)))
    else: shots.append(shot("mil_"+k,b,dayT=dt,n=n,wait=2500,js=notraf+CAR+(PAN if k in('gagne',) else NOPAN)))
  ev="(()=>{const g=window.__CC;return g?{par:!!g.parent,vis:g.visible,pos:[g.position.x,g.position.z],em:(g.userData.nacre||{}).em}:'nocar'})()"
  out='/root/cap/mil'+('f' if mode=='f' else 'r')
  print(run(shots,out,w=1080 if mode=='f' else 540,h=1920 if mode=='f' else 960,ev=ev,wait=False))
