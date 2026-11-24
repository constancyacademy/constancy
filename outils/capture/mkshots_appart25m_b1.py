# appart25m_b2 (M4 NUIT jeu. 26/11 21h) · repris de mkshots_appart25m_b1.py (repérage du 24/11 21h30)
import os,math
DT=int(os.environ.get("DT","900"))
PLAYW="{const W6=window.__W();if(!window.__stepP){const s0=window.__step;window.__step=ms=>{W6.G.mode='play';return s0(ms);};window.__stepP=1;}const F=window.__FW;window.__fwBig=1;F.party=30;F.pts.visible=true;}"
TAKE="{const W6=window.__W();if(!window.__APG){const a=(W6.AGENCE||[]).find(x=>x.id=='penthouse');W6.startVisit(a);}}"
TAKE2="{const W6=window.__W();if(W6.VISIT.on){window.__APG=W6.VISIT.g;W6.VISIT.on=false;}W6.G.mode='play';W6.G.fpv=false;document.body.classList.remove('lifting');const u=document.getElementById('visitUI');if(u)u.style.display='none';}"
FWK="{const F=window.__FW;if(F){if(!(F.party>5))F.party=30;if(F.next>0.45)F.next=0.45;}window.__fwBig=1;}"
ME="{const W6=window.__W();const T6=W6.TOWER;W6.G.me.x=T6.x+200;W6.G.me.z=T6.z+20;W6.G.onFoot=true;}"
def LLT(p,t,fov=62):
  # p, t : triplets d'expressions JS (T = temps du plan en s), coordonnées locales de l'appartement
  return ("const g=window.__APG;if(!g)return {p:[0,400,0],t:[0,0,0],fov:60};const A=g.localToWorld(new THREE.Vector3(%s,%s,%s)),B=g.localToWorld(new THREE.Vector3(%s,%s,%s));"
          "return {p:[A.x,A.y,A.z],t:[B.x,B.y,B.z],fov:%s};")%(tuple("(%s)"%x for x in p)+tuple("(%s)"%x for x in t)+(fov,))
def MK(name,body,n=1,o=0,js="",wait=2500):
  s=shot(name,FWK+body,dayT=DT,n=n,toff=o,wait=wait,js=NO+NOPLANE+PLAYW+TAKE+ME+js); s["camjs"]=s["camjs"].replace("{const T=","{"+TAKE2+"const T=",1) if False else s["camjs"]; s["far"]=20000
  s["js"]+=";setTimeout(()=>{"+TAKE2+"},600);"
  return s
S={}
# 1 : avance vers la baie, plongée 24°
S["A1"]=LLT(("0.8","1.7","3.6+0.9*T"),("0.8+0.6*T","-24","60"))
S["A1b"]=LLT(("-2.5","1.75","4.0+0.8*T"),("-1.5","-30","60"))
# 2 : salon vu du fond, la baie et la ville
S["B1"]=LLT(("-9.5+0.5*T","2.3","-6.0"),("4","0.6","8"),66)
S["B2"]=LLT(("9.5-0.5*T","2.3","-6.0"),("-4","0.6","8"),66)
S["B3"]=LLT(("-3+0.6*T","2.0","-6.8"),("0","1.0","8"),70)
# 3 : collé à la vitre, plongée sur la ville
S["C1"]=LLT(("1.3","1.7","7.2"),("8+3*T","-120","60"))
S["C2"]=LLT(("-6","1.7","7.0"),("-2","-90","70"))
# 4 : vitre de côté (nord/sud)
S["E1"]=LLT(("10.6","1.7","2"),("60","-40","10"))
S["E2"]=LLT(("-10.6","1.7","2"),("-60","-40","10"))
NEAR="{const W6=window.__W();const c=W6.camera;if(!c.__nearP){Object.defineProperty(c,'near',{configurable:true,get:()=>window.__NEARV||0.8,set:v=>{}});c.__nearP=1;}window.__NEARV=0.8;c.updateProjectionMatrix();}"
S["A2"]=LLT(("0.8","1.7","3.6+0.9*T"),("0.8+0.6*T","-14","60"))
S["A3"]=LLT(("-1.2","1.7","4.5+0.7*T"),("-1.2","-20","60"),66)
S["B4"]=LLT(("-9.5+0.5*T","2.6","-6.0"),("3","-1.2","8"),62)
S["D1"]=LLT(("8.5","1.7","5.5"),("-20","-18","60"),66)
S["E3"]=LLT(("10.8","1.7","-5"),("40","-15","-40"),66)
S["E4"]=LLT(("-10.8","1.7","-5"),("-40","-15","-40"),66)
S["E5"]=LLT(("10.8","1.7","4"),("50","-30","0"),66)
S["X1"]=LLT(("6","4","40"),("0","1.5","0"),55)
S["B5"]=LLT(("0","1.5","-7.3"),("0","1.0","8"),75)
S["X2"]=LLT(("14-4*T","1.0","34-1.5*T"),("-2","2.2","0"),55)
S["X3"]=LLT(("-16+5*T","-3","30"),("0","2.0","0"),58)
S["B6"]=LLT(("-11+0.8*T","1.5","6.3"),("12","0.9","4.2"),70)
S["B7"]=LLT(("4","1.3","-4.5+0.5*T"),("-6","1.2","8"),66)
S["FA"]=LLT(("0.8","1.7","3.2+0.8*T"),("0.8+0.5*T","-14","60"),62)
S["FX"]=LLT(("14-4*T","1.0","34-1.5*T"),("-2","2.2","0"),55)
S["FB"]=LLT(("4.5-0.6*T","1.0","-4.0"),("-5","1.9","8"),66)
S["FE"]=LLT(("-18+4*T","-2+1.5*T","32"),("0","-10","0"),58)
S["G1"]=LLT(("-3.0+1.1*T","1.7","6.4+0.25*T"),("-1.5+1.1*T","-22","60"),62)
S["G2"]=LLT(("4.0-0.9*T","1.75","6.9"),("6-0.9*T","-28","60"),60)
U="(T-2.5167)"
S["G1b"]=LLT(("-3.2+1.0*"+U,"1.7","6.25+0.2*"+U),("-1.7+1.0*"+U,"-17","60"),62)
