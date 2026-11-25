exec(open('/home/claude/rushes/outils/capture/mkshots_panorama_b1.py').read())
# panorama_b3 (24/11 nuit) · corrections du verdict de 23h05 · 60 i/s capturés
SIGNOFF="{const W6=window.__W();W6.scene.traverse(o=>{if(o.isMesh&&o.material&&o.material.map&&o.material.map.image&&o.material.map.image.width===1024&&o.material.map.image.height===300&&o.material.side===2&&o.parent&&!o.parent.__hid){const p=o.parent;p.__hid=1;Object.defineProperty(p,'visible',{configurable:true,get:()=>false,set:()=>{}});}});}"
P=lambda pre: "const U=T-%f;"%((pre+1)/60.0)
def MK3(name,body,n=1,js="",pre=150,wait=2500):
  s=MK(name,PLAY+body,n=n,js=PLAYW+SIGNOFF+js,wait=wait); s["fps"]=60; s["pre"]=pre; return s
S["P1"]=P(150)+FWB+FWP+FWK+L(("260-80*U","50","220"),("0-14*U","165","-10"),60)
S["P1b"]=P(150)+FWB+FWP+FWK+L(("230-75*U","40","150-10*U"),("20","150","-10"),58)
S["P2"]=P(60)+bridge(13.5,725,-22).replace("*T","*U")+L(("cx+0.9","cy+6.0","cz+14"),("cx-0.4","cy+1.2","cz-60"),58)
ROOF="const RA=-2.4+0.35*U;"
S["P3"]=P(150)+FWB+FWP+FWK+ROOF+L(("84+15*Math.cos(RA)","74","28+15*Math.sin(RA)"),("84","70.5","28"),60)
S["P3b"]=P(150)+FWB+FWP+FWK+ROOF+L(("84+17*Math.cos(RA)","78","28+17*Math.sin(RA)"),("84-30*Math.cos(RA)","60","28-30*Math.sin(RA)"),62)
S["P1f"]=P(300)+FWB+FWP+FWK+L(("260-80*U","50","220"),("0-14*U","165","-10"),60)
S["P2f"]=S["P2"]
ROOF2="const RA=0.55+0.10*U;"
S["P3f"]=P(300)+FWB+FWP+FWK+ROOF2+L(("84+16*Math.cos(RA)","76","28+16*Math.sin(RA)"),("84","73","28"),62)
def BURST(x,y,z,t,key):
  return ("{const F=window.__FW;if(F&&F.pos&&U>=%f&&!window.%s){window.%s=1;const i=F.i=(F.i+1)%%F.n,k=i*3;F.pos[k]=%f;F.pos[k+1]=%f;F.pos[k+2]=%f;F.v[k]=0;F.v[k+1]=0.5;F.v[k+2]=0;F.life[i]=F.max[i]=0.02;F.base[k]=1;F.base[k+1]=.8;F.base[k+2]=.5;F.kind[i]=1;F.sz[i]=1.4;}}")%(t,key,key,x,y,z)
RB="if(T<0.2){window.__b1=0;window.__b2=0;window.__b3=0;}"
S["P1g"]=P(150)+RB+FWB+FWP+FWK+BURST(150,135,80,0.0,"__b1")+BURST(60,150,40,0.55,"__b2")+BURST(170,110,10,1.15,"__b3")+L(("260-80*U","50","220"),("0-14*U","165","-10"),60)
S["M1"]=P(30)+L(("-60+25*U","330","-2230"),("0","120","-600"),58)
S["M2"]=P(30)+L(("80-20*U","300","-1900"),("0","60","0"),58)
S["M3"]=P(30)+MONTB+L(("40","310+8*U","-2120"),("0","90","-300"),60)
