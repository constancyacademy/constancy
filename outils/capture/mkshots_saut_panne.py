from h import *
import sys
SETUP="""{const W7=window.__W();if(!window.__PL){const g=W7.makeRide('avion');W7.scene.add(g);window.__PL=g;
 const c=document.createElement('canvas');c.width=c.height=64;const x=c.getContext('2d');const gr=x.createRadialGradient(32,32,0,32,32,32);gr.addColorStop(0,'rgba(70,70,74,0.95)');gr.addColorStop(0.5,'rgba(90,90,95,0.55)');gr.addColorStop(1,'rgba(110,110,115,0)');x.fillStyle=gr;x.fillRect(0,0,64,64);
 const tx=new THREE.CanvasTexture(c);window.__SM=[];for(let i=0;i<140;i++){const s=new THREE.Sprite(new THREE.SpriteMaterial({map:tx,transparent:true,depthWrite:false}));s.visible=false;W7.scene.add(s);window.__SM.push(s);}}
 window.__PL.visible=true;}"""
BODY="""const PL=window.__PL;const X0=-30,Z0=750,A0=1110,V=46;
const PIT=t=>{const k=Math.max(0,Math.min(1,(t-%(td)s)/1.1));return 0.06-0.62*k*k*(3-2*k);};
const POS=t=>{let x=X0,z=Z0,a=A0;const n=Math.max(1,Math.round(t*60));const dt=t/n;for(let i=0;i<n;i++){const p=PIT(i*dt);z-=V*Math.cos(p)*dt;a+=V*Math.sin(p)*dt;}return [x,a,z];};
const P=POS(T),p=PIT(T);PL.rotation.order='YXZ';PL.position.set(P[0],P[1],P[2]);PL.rotation.set(-p,Math.PI,0.04*Math.sin(T*9)*Math.max(0,T-%(td)s));
const SM=window.__SM;for(let i=0;i<SM.length;i++){const ti=%(ts)s+i*0.011;const s=SM[i];if(T<ti){s.visible=false;continue;}const age=T-ti;const q=POS(ti),pp=PIT(ti);const nx=q[0],ny=q[1]+0.4+Math.sin(pp)*2.6,nz=q[2]-Math.cos(pp)*2.6;
 const j1=Math.sin(i*12.9898)*0.5,j2=Math.sin(i*78.233)*0.5;s.position.set(nx+j1*0.8+j1*1.5*age,ny+j2*0.5+1.6*age,nz+j2*0.8);const sc=1.6+5.5*age+j1;s.scale.set(sc,sc,1);s.material.opacity=Math.max(0,0.8-0.5*age);s.visible=true;}
%(cam)s"""
CAMS={
"chase":"return {p:[P[0]+1.5,P[1]+6,P[2]+18],t:[P[0],P[1]-3,P[2]-25],fov:62};",
"cote":"return {p:[P[0]+20,P[1]+3,P[2]-4],t:[P[0],P[1]-2,P[2]-2],fov:58};",
}
def body(cam,td=0.25,ts=0.0): return BODY%{"td":td,"ts":ts,"cam":CAMS[cam]}
if __name__=="__main__":
  sel=sys.argv[1].split(','); toffs=[float(x) for x in sys.argv[2].split(',')]
  shots=[shot("%s_t%02d"%(k,int(t*10)),body(k),dayT=500,toff=t,wait=1500,js=notraf+SETUP) for k in sel for t in toffs]
  for s in shots: s["far"]=6000
  print(run(shots,'/root/cap/pn',wait=False))

def full():
  sh=shot("saut_panne_jour",body("chase",td=0.1,ts=0.0),dayT=500,n=31,wait=2500,js=notraf+SETUP); sh["far"]=6000
  print(run([sh],'/root/cap/pnf',w=1080,h=1920,wait=False))
