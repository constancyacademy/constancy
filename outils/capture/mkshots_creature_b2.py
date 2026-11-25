# creature_b2 (25/11 15h30, monteur) : corrections du verdict de l'expert du 25/11 13h50 (Rex entier entre la bulle et la carte, ouverture vivante, Rex éclairé, poteau hors cadre)
exec(open('/home/claude/rushes/outils/capture/mkshots_creature_b1.py').read())
S["O1"]=camA(1.0,"0.58+0.10*T","66-3.0*T",2.5,"Head",0.42,0.42,64)
S["O2"]=camA(1.0,"0.75-0.10*T","66-3.0*T",2.0,"Head",0.45,0.42,62)
S["O3"]=camA(1.0,0.50,"68-3.5*T",3,"EYES",0.5,0.40,60)
S["L1"]=camA(1.0,1.0,"46-1.5*T",14,"EYES",0.5,0.45,55)
S["L2"]=camA(1.0,0.75,"44-1.5*T",10,"EYES",0.45,0.40,58)
S["L3"]=camA(1.0,1.4,"46-1.5*T",12,"EYES",0.5,0.42,55)
S["L4"]=camA(1.0,0.5,"40",8,"Head",0.5,0.40,60)
S["Fa"]=camA(1.0,"1.9-0.27*T",50,6,"L_Foot",0.5,0.58,72)
S["Fb"]=camA(1.0,"2.1-0.3*T",50,8,"L_Foot",0.5,0.58,66)
S["Fc"]=camA(1.0,"-1.9+0.27*T",50,6,"L_Foot",0.5,0.58,72)
S["O4"]=camA(1.0,1.10,"64-2.5*T",3,"EYES",0.5,0.40,60)
S["O5"]=camA(1.0,1.25,"64-2.5*T",3,"EYES",0.5,0.40,60)
S["O6"]=camA(1.0,1.40,"64-2.5*T",3,"EYES",0.5,0.40,60)
S["Fd"]=camA(1.0,"2.0-0.15*T",52,9,"L_Foot",0.5,0.62,84)
S["Fe"]=camA(1.0,"2.0-0.15*T",52,12,"L_Foot",0.5,0.62,80)
S["Ff"]=camA(1.0,"1.95-0.12*T",52,10,"L_Foot",0.5,0.62,88)
S["L5"]=camA(1.0,1.6,"48-1.5*T",12,"EYES",0.5,0.42,55)
S["L6"]=camA(1.0,1.25,"46-1.5*T",16,"EYES",0.5,0.45,52)
# projecteur de face (lumière posée 6 m au-dessus de la caméra, suit la caméra) : LT(i) dans le js, LC(corps) dans la caméra
def LT(i): return "{const W6=window.__W();if(!window.__LT){window.__LT=new THREE.PointLight(0xffe6f2,0,140,1.0);W6.scene.add(window.__LT);}window.__LT.intensity=%s;}"%i
def LC(body): return body.replace("return {p,","window.__LT&&window.__LT.position.set(p[0],p[1]+6,p[2]);return {p,")
S["Fg"]=camA(1.0,"2.0-0.12*T",52,11,"L_Foot",0.5,0.57,"(90+3*T)")
S["O7"]=camA(1.0,1.12,"60.5-1.8*T",3,"EYES",0.5,0.40,60)
for k in ["L3","L5","Fg"]: S[k+"x"]=LC(S[k])
LJ={"L3x":2.2,"L5x":2.2,"Fgx":1.6}
_MK2=MK
def MK(name,body,n=1,o=0,js="",wait=2500):
  k=[x for x in LJ if S[x]==body]
  return _MK2(name,body,n=n,o=o,js=js+LT(LJ[k[0]] if k else 0),wait=wait)
# projecteur posé devant le Rex, côté caméra (18 m devant lui, 14 m de haut) : pelouse près de la caméra pas éclairée
def LC2(body): return body.replace("return {p,","{const dx=p[0]-P.x,dz=p[2]-P.z,dl=Math.hypot(dx,dz)||1;window.__LT&&window.__LT.position.set(P.x+dx/dl*18,P.y+14,P.z+dz/dl*18);}return {p,")
S["Fh"]=LC2(camA(1.0,"2.0-0.12*T",52,11,"L_Foot",0.5,0.60,"(90+3*T)"))
S["O7x"]=LC(S["O7"])
LJ.update({"Fh":1.6,"O7x":2.2})
S["O7y"]=LC(camA(1.0,1.12,"60-1.6*T",3,"EYES",0.5,0.40,54))
LJ.update({"O7y":2.2})
