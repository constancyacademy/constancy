import json,sys
hide=open('/home/claude/rushes/outils/capture/hide.js').read().strip()
fix="try{const W2=window.__W();Object.values(W2.beacons||{}).forEach(b=>{if(b)b.visible=false;});if(W2.destBeacon)W2.destBeacon.visible=false;if(W2.ownMark)W2.ownMark.visible=false;}catch(e){} const DK=window.__MAPB().DK; DK.cars.forEach((c,k)=>{ c.lane = (k%2? c.D.w*0.28 : 0.001); c.sp=1.0; });"
# common JS helpers inside camjs
H="""const DK=window.__MAPB().DK;const L=(a,b,k)=>a.map((v,i)=>v+(b[i]-v)*k);const E=k=>k<0?0:k>1?1:(1-Math.pow(1-k,2));
const PS=(S,s)=>{let i=0;while(i<S.length-2&&S[i+1][3]<s)i++;const a=S[i],b=S[i+1],t=(s-a[3])/Math.max(1e-6,b[3]-a[3]);return [a[0]+(b[0]-a[0])*t,a[2]+(b[2]-a[2])*t,a[1]+(b[1]-a[1])*t];};
const NEAR=(S,X,Z)=>{let bi=0,bd=1e9;S.forEach((p,i)=>{const d=Math.hypot(p[0]-X,p[1]-Z);if(d<bd){bd=d;bi=i;}});return S[bi][3];};
const CARN=(nm,k,X,Z,lead)=>{const cs=DK.cars.filter(c=>c.D.name.startsWith(nm));const c=cs[k%cs.length],S=c.D.S,Lt=S[S.length-1][3];if(window.__T0==null){c.sp=1.0;c.u=((NEAR(S,X,Z)-lead)/Lt+1)%1;}return {c,S,Lt,s:c.u*Lt};};
const CAR=(ci,U0,TT)=>{const c=DK.cars[ci],S=c.D.S,Lt=S[S.length-1][3];if(window.__T0==null){c.u=U0;}return {c,S,Lt,s:c.u*Lt};};"""
def camjs(body,toff=0):
  return "(G)=>{const T=(performance.now()-(window.__T0||performance.now()))/1000+%s;%s%s}"%(toff,H,body)
SH={
"G":"const k=T;const d=[0.7071,-0.7071],n=[0.7071,0.7071];const c0=[595+n[0]*48-d[0]*40,595+n[1]*48-d[1]*40];const cx=c0[0]+d[0]*32*k,cz=c0[1]+d[1]*32*k;return {p:[cx,36,cz],t:[cx-n[0]*48+d[0]*10,24,cz-n[1]*48+d[1]*10],fov:58};",
"H":"const k=T/1.5;return {p:L([735,7,538],[585,9,355],k),t:L([520,16,275],[440,20,180],k),fov:66};",
"A":"const k=E(T/1.9);return {p:L([905,100,352],[735,40,298],k),t:L([520,14,250],[470,16,236],k),fov:62};",
"B":"const o=CARN('Bretelle de l',0,586,365,14);const s=o.s;const p=PS(o.S,s),q=PS(o.S,s+8);const P0=PS(o.S,o.s);const a=PS(o.S,NEAR(o.S,560,350)),b=PS(o.S,NEAR(o.S,612,380));const hx=b[0]-a[0],hz=b[2]-a[2],hl=Math.hypot(hx,hz);const rx=hz/hl,rz=-hx/hl;return {p:[p[0]+rx*26-hx/hl*4,p[1]+5,p[2]+rz*26-hz/hl*4],t:[q[0],q[1]+0.5,q[2]],fov:56};",
"F":"const o=CARN('Bretelle de l',1,586,365,30);const a=PS(o.S,NEAR(o.S,560,350)),b=PS(o.S,NEAR(o.S,612,380));const hx=b[0]-a[0],hz=b[2]-a[2],hl=Math.hypot(hx,hz);const rx=hz/hl,rz=-hx/hl;const m=PS(o.S,NEAR(o.S,586,365));const k=T/1.15;return {p:[m[0]+rx*16-hx/hl*(10-12*k),4+38*k,m[2]+rz*16-hz/hl*(10-12*k)],t:[m[0]+hx/hl*6,18+15*k,m[2]+hz/hl*6],fov:66};",
"C":"const k=0.18+T/1.4;return {p:L([560,3.5,300],[628,5,352],k),t:L([660,34,380],[700,40,420],k),fov:70};",
"D":"const o=CAR(0,0.08);const s=o.s;const p=PS(o.S,s-14+5*T),q=PS(o.S,s+26);return {p:[p[0],p[1]+4.2,p[2]],t:[q[0],q[1]+1.5,q[2]],fov:64};",
"E":"const k=T/1.6;return {p:L([1060,205,700],[950,170,520],k),t:L([380,0,140],[360,0,80],k),fov:60};",
}
mode=sys.argv[1]
shots=[]
if mode=="scout":
  dt=int(sys.argv[2])
  for n,b in SH.items():
    for toff in (0,0.7,1.4):
      shots.append({"name":"%s%d"%(n,int(toff*10)),"n":1,"one":True,"wait":2500,"dayT":dt,"js":hide+fix,"camjs":camjs(b,toff)})
  shots[0]["wait"]=15000
  w,h=540,960
else:
  dt=int(sys.argv[2]); nf=int(sys.argv[3]); names=sys.argv[4].split(",")
  for n in names:
    shots.append({"name":n,"n":nf,"wait":3000,"dayT":dt,"js":hide+fix,"camjs":camjs(SH[n])})
  shots[0]["wait"]=15000
  w,h=1080,1920
json.dump({"url":"file:///home/claude/constancy/index.html?nostat=1","w":w,"h":h,"shots":shots},open(sys.argv[-1],'w'))
