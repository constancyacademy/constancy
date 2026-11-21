from h import *
import sys,math
STAR="""window.__fxBoost=1;const ST=(i,t0,life,dAz,el,sgn,p,t,sp,R)=>{R=R||1500;const N=window.__W().NSKY;N.next=999;if(!N.pool)return;const S=N.pool[i];const tt=T-t0;if(tt<0||tt>life){S.on=false;S.m.visible=false;S.h.visible=false;return;}const yaw=Math.atan2(t[2]-p[2],t[0]-p[0])+dAz;const d=new THREE.Vector3(Math.cos(yaw)*Math.cos(el),Math.sin(el),Math.sin(yaw)*Math.cos(el));const sd=new THREE.Vector3(-Math.sin(yaw)*sgn,-0.16,Math.cos(yaw)*sgn).normalize();S.on=true;S.p=d.multiplyScalar(R);S.v=sd.multiplyScalar((sp||900)*R/1500);S.t=tt;S.life=life;};const OFF=()=>{const N=window.__W().NSKY;N.next=999;if(N.pool)N.pool.forEach(S=>{S.on=false;S.m.visible=false;S.h.visible=false;});};"""
def sh(p,t,fov,stars):
  s="const p=%s,t=%s;"%(p,t)
  for st in stars:
    i,t0,life,daz,el,sgn=st[:6]; R=st[6] if len(st)>6 else 1500
    s+="ST(%d,%f,%f,%f,%f,%d,p,t,900,%f);"%(i,t0,life,daz,el,sgn,R)
  return s+"return {p:p,t:t,fov:%s};"%fov
S={
"tours":sh("[56,2+7*T,56]","[20,70+8*T,-40]",62,[(0,0.0,1.4,-0.33,0.75,1)]),
"toursB":sh("[112,3+8*T,112]","[40,120+6*T,-10]",62,[(0,0.0,1.4,0.15,0.9,1)]),
"toursC":sh("[0,3+8*T,112]","[28,140+6*T,-28]",62,[(0,0.0,1.4,-0.4,0.95,1)]),
"toursD":sh("[112,3+8*T,112]","[40,120+6*T,-10]",62,[(0,0.0,1.4,-0.3,0.85,1,650)]),
"eau":sh("[-760-6*T,1.3,430]","[-1150,35,330]",60,[(0,0.0,1.3,0.33,0.42,-1)]),
"toit":sh("[40-3*T,186,40-3*T]","[260,110,330]",62,[(0,0.0,1.3,-0.33,0.3,1)]),
"mont":sh("[0+8*T,320,-1950+6*T]","[0,120,-200]",60,[(0,0.1,1.3,0.2,0.2,-1),(1,0.35,1.2,-0.15,0.3,-1)]),
}
sel=sys.argv[1].split(','); toffs=[float(x) for x in sys.argv[2].split(',')]
shots=[]
for k in sel:
  for t in toffs: shots.append(shot("%s_t%02d"%(k,int(t*10)),S[k],dayT=840,toff=t,wait=1500,js=notraf,pre=STAR))
ev="(()=>{const W=window.__W();return {tw:W.TOWER, pool:!!W.NSKY.pool, nk:W.nightK}})()"
print(run(shots,'/root/cap/s2',ev=ev,wait=False))
