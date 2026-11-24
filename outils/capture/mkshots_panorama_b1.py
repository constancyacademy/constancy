# panorama_b1 (jeu. 26/11 7h, M1 VRAI 3D, COMMANDE de l'expert du 24/11 19h45) · « Un monde ouvert. Sur ton téléphone. »
# 3 plans en mouvement : skyline néon + feu d'artifice (travelling latéral) · F10 avec une voiture phares allumés, ville derrière · Mont Constantine et ses faisceaux, caméra qui se lève
import os,math
DT=int(os.environ.get("DT","840"))
def L(p,t,fov=60): return "return {p:[%s,%s,%s],t:[%s,%s,%s],fov:%s};"%(tuple(p)+tuple(t)+(fov,))
UNFPV="{const W6=window.__W();W6.G.fpv=false;W6.G.mode='play';}"
FWON="{window.__FW&&window.__FW.pts&&(window.__FW.pts.visible=true);}"
FWK="{const F=window.__FW;if(F&&F.next>0.45)F.next=0.45;}"
CARN="{const W9=window.__W();if(!window.__PNC){const g=W9.makeCar(W9.CARS.find(c=>c.id=='hyper'));W9.scene.add(g);window.__PNC=g;}W9.scene.traverse(o=>{if(o.userData&&o.userData.isCar&&o!==window.__PNC&&!o.__hid){o.__hid=1;Object.defineProperty(o,'visible',{configurable:true,get:()=>false,set:()=>{}});}});delete window.__PNC.visible;window.__PNC.visible=true;window.__lt=null;}"
NOCAR="{if(window.__PNC){window.__PNC.visible=false;}}"
def MK(name,body,n=1,o=0,js="",wait=2500):
  fw=FWON if "FWK" in body or "__FWK" in name else ""
  extra=CARN if "__PNC" in body else NOCAR
  s=shot(name,body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+UNFPV+HIDELIGHTS+notraf+extra+FWON+js); s["far"]=20000; return s
DKF=("const W7=window.__W();const S=(window.__F10S=window.__F10S||W7.DK.decks.find(q=>q.name.indexOf('F10')>=0).S);"
     "const at=(d,off)=>{let i=0;while(i<S.length-2&&S[i+1][3]<d)i++;const a=S[i],b=S[i+1];const t=(d-a[3])/(b[3]-a[3]);"
     "let dx=b[0]-a[0],dz=b[1]-a[1];const l=Math.hypot(dx,dz);dx/=l;dz/=l;const x=a[0]+(b[0]-a[0])*t-dz*off,z=a[1]+(b[1]-a[1])*t+dx*off,y=a[2]+(b[2]-a[2])*t;return {x,y,z,dx,dz,sl:(b[2]-a[2])/l};};")
def car_f10(d0,v,off=3.0,sgn=1):
  return DKF+("const g=window.__PNC;const C=at(%f+(%f)*T,%f);const cx=C.x,cy=C.y+0.12,cz=C.z;g.position.set(cx,cy,cz);g.rotation.order='YXZ';"
     "g.rotation.y=Math.atan2(%d*C.dx,%d*C.dz);g.rotation.x=-Math.atan(%d*C.sl);"
     "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(d0,sgn*v,sgn*off,sgn,sgn,sgn,abs(v))
S={}
# A · skyline + feu d'artifice, travelling latéral
S["A1"]=FWK+L(("-200+35*T","45","560"),("0+10*T","120","0"),55)
S["A2"]=FWK+L(("250-35*T","30","380"),("0","110","-20"),55)
S["A3"]=FWK+L(("-700","40","100+30*T"),("0","120","0"),55)
S["A4"]=FWK+L(("-120+40*T","18","330"),("10+10*T","120","0"),60)
# B · F10 (repérage sans voiture)
S["B0"]=L(("0","8","790"),("0","60","0"),58)
S["B1"]=DKF+"const K=at(900,0);"+L(("K.x","K.y+6","K.z"),("K.x","K.y+40","K.z-600"),58)
# C · Mont Constantine
S["C1"]=L(("60","80+25*T","-1600"),("0","180+15*T","-2050"),55)
S["C2"]=L(("0+20*T","40+30*T","-1450"),("0","230","-2050"),55)
S["C3"]=L(("-250","60+25*T","-1700"),("0","200","-2050"),55)
# feu d'artifice nourri au-dessus du centre (fête du jeu : FW.party, tirs près du joueur au centre et sur la tour)
FWP="{const F=window.__FW;if(F){if(!(F.party>5))F.party=30;}}"
S["A5"]=FWP+FWK+L(("-200+35*T","45","560"),("0+10*T","120","0"),55)
S["A6"]=FWP+FWK+L(("-120+40*T","18","330"),("10+10*T","120","0"),60)
S["A7"]=FWP+FWK+L(("-260+45*T","60","480"),("-20+12*T","140","0"),52)
def bridge(x,z0,vz):
  ry=0 if vz>0 else math.pi
  return ("const W7=window.__W();const g=window.__PNC;const D=W7.DK.decks.find(d=>d.name===\"Pont de l'Esplanade\").S;const cx=%f,cz=%f+(%f)*T;let cy=D[0][2];for(let i=1;i<D.length;i++){if(D[i][1]>=cz){const a=D[i-1],b=D[i],k=(cz-a[1])/(b[1]-a[1]);cy=a[2]+(b[2]-a[2])*k;break;}cy=D[i][2];}cy+=0.12;"
          "g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,%f,0,T-window.__lt);}window.__lt=T;")%(x,z0,vz,ry,abs(vz))
S["B2"]=bridge(13.5,725,-22)+L(("cx+3","cy+4.5","cz+13"),("cx-1","cy+3","cz-40"),58)
S["B3"]=bridge(13.5,725,-22)+L(("cx-9","cy+2.2","cz-16"),("cx","cy+0.8","cz"),58)
S["B4"]=bridge(13.5,725,-22)+L(("cx+7","cy+1.5","cz+9"),("cx-2","cy+6","cz-60"),56)
S["C4"]=L(("40","35","-1560"),("0","120+40*T","-2050"),55)
S["C5"]=L(("-60+15*T","45","-1480"),("0","150+35*T","-2100"),52)
FWB="{window.__fwBig=1;}"
S["A8"]=FWB+FWP+FWK+L(("-160+40*T","35","270"),("0+10*T","175","0"),58)
S["A9"]=FWB+FWK+L(("-160+40*T","35","270"),("0+10*T","175","0"),58)
S["A10"]=FWB+FWP+FWK+L(("260-40*T","50","220"),("0-8*T","165","-10"),60)
S["B5"]=bridge(13.5,725,-22)+L(("cx+2.5","cy+3.2","cz+10"),("cx-0.5","cy+4","cz-50"),58)
S["C6"]=L(("-600","40","-2200"),("0","150","-2300"),55)
S["C7"]=L(("500","40","-2450"),("0","150","-2300"),55)
S["C8"]=L(("0","45","-2600"),("0","150","-2050"),55)
# faisceaux du Mont (4 Meshes additifs de 900 m sur la face nord, z -1926) : cachés par hide.js, remis visibles ici
MONTB="{const W6=window.__W();W6.scene.traverse(o=>{if(o.isMesh&&o.material&&o.material.blending===2&&o.geometry&&o.geometry.parameters&&o.geometry.parameters.height===900)o.visible=true;});}"
S["C9"]=MONTB+L(("60","40","-1500"),("0","160+40*T","-2000"),55)
S["C10"]=MONTB+L(("-40+10*T","30+8*T","-1450"),("0","200+40*T","-2050"),55)
S["C11"]=MONTB+L(("200-25*T","35","-1550"),("0","180+30*T","-2000"),55)
S["B6"]=bridge(13.5,725,-22)+L(("cx+0.9","cy+3.4","cz+10"),("cx-0.4","cy+3.6","cz-50"),58)
STAR="{const W6=window.__W();if(T<0.04&&W6.NSKY&&W6.NSKY.next>0.6)W6.NSKY.next=0.6;}"
S["B7"]=bridge(13.5,725,-22)+L(("cx+0.9","cy+6.0","cz+14"),("cx-0.4","cy+1.2","cz-60"),58)
S["C12"]=MONTB+STAR+L(("60","40+6*T","-1500"),("0","210+35*T","-2000"),55)
# rendu final (24/11 20h10)
S["Af"]=S["A10"]
S["Bf"]=S["B7"]
S["Cf"]=MONTB+STAR+L(("60","40+6*T","-1500"),("0","230+35*T","-2000"),55)
S["Df"]=S["A8"]
# 24/11 19h55 : les fusées mettent ~5 s à monter (rien d'éclaté dans un plan filmé depuis T = 0) → plans A et D filmés avec 5,5 s de pré-roulage (toff), Mont avec plus de mouvement
S["Cg"]=MONTB+STAR+L(("150-40*T","35+12*T","-1480"),("0","200+40*T","-2000"),55)
# NB : avec fin_monteur o > 0, T dans la caméra = temps écoulé + o (donc 2 × o + 0,13 à la 1re image) → caméra recalée sur U = T - 2 × o
def UF(body,o): return "const U=T-%f;"%(2*o)+body.replace("*T","*U")
S["Af2"]=UF(S["A10"],5.5)
S["Df2"]=UF(S["A8"],5.5)
# 24/11 20h15 : feux d'artifice figés en prise (G.mode repasse à « email » entre deux images, la mise à jour des fusées s'arrête) → G.mode='play' à chaque image + 5 s de pré-roulage (pre 150)
PLAY="{const W6=window.__W();W6.G.mode='play';}"
S["Af3"]=PLAY+"const U=T-10.4;"+S["A10"].replace("*T","*U")
S["Df3"]=PLAY+"const U=T-10.4;"+S["A8"].replace("*T","*U")
# 24/11 20h40 (diagnostic) : les fusées montent bien en prise figée SI G.mode = 'play' avant chaque pas (sinon le jeu repasse à « email » et fige les fusées)
# → __step enveloppé (G.mode='play' avant chaque pas) + 5 s de pré-roulage faites dans le js du plan
PREFW="{const W6=window.__W();if(!window.__stepP){const s0=window.__step;window.__step=ms=>{W6.G.mode='play';return s0(ms);};window.__stepP=1;}const F=window.__FW;window.__fwBig=1;F.party=30;F.pts.visible=true;window.__freeze();for(let k=0;k<150;k++){window.__step(1000/30);}window.__unfreeze();}"
# 20h45 : le pré-roulage DANS le js (gel puis dégel) fait reculer l'horloge de 5 s au dégel et tue les fusées → pré-roulage par « pre » du démon (pas de dégel), __step enveloppé (play)
PLAYW="{const W6=window.__W();if(!window.__stepP){const s0=window.__step;window.__step=ms=>{W6.G.mode='play';return s0(ms);};window.__stepP=1;}const F=window.__FW;window.__fwBig=1;F.party=30;F.pts.visible=true;}"
