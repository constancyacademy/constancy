HY=("{const W9=window.__W();if(!window.__HY){const g=W9.makeCar(W9.CARS.find(c=>c.id=='hyper'));W9.scene.add(g);window.__HY=g;}"
 "delete window.__HY.visible;window.__HY.visible=true;window.__lt=null;window.__CYE=0;}")
def CARX(x0,z,v,a=0,dirx=-1):
  return ("const g=window.__HY;const d=%f*T+0.5*(%f)*T*T,vv=Math.max(0,%f+(%f)*T);const cx=%f+(%d)*d,cz=%f;const cy=W7.GH(cx,cz);g.position.set(cx,cy,cz);g.rotation.order='YXZ';g.rotation.y=%f;"
          "if(window.__lt!=null&&T>window.__lt){W7.spinWheels(g,vv,0,T-window.__lt);}window.__lt=T;")%(v,a,v,a,x0,dirx,z,(-1.5708 if dirx<0 else 1.5708))
PPL=("{const W9=window.__W();const pts=[[48,6.5],[54,7.5],[60,6.5]];(W9.CY.ppl||[]).forEach((q,k)=>{const p=pts[k];if(!p)return;const y=W9.GH(p[0],p[1]);if(q.m){q.m.position.set(p[0],y+0.02,p[1]);q.m.rotation.y=Math.PI;}if(q.b)q.b.position.set(p[0],y,p[1]);q.x=p[0];q.z=p[1];});}")
S["B1"]=TOR("330-6*T","0")+CARX(70,-1.8,20)+L(("cx-9+3*T","cy+1.0","cz+1.2"),("cx+40","cy+8","cz"),62)
S["C1"]=TOR("330-6*T","0")+CARX(100,-1.8,14,-5.5)+L(("cx-14","cy+16","cz-14"),("cx+4","cy","cz+3"),58)
S["D1"]="if(!window.__CYE&&T>0){window.__CYE=1;W7.cyEnd(true);}W7.WX.rain=Math.max(0,0.8-0.35*T);"+TOR("300","0")+L(("-80","70","-60"),("260","80","10"),58)
JS={"B1":HY,"C1":HY+PPL,"D1":HY}
_MK=MK
def MK(name,body,n=1,o=0,js="",wait=3000):
  k=[x for x in JS if S[x]==body]
  return _MK(name,"const W7=window.__W();"+body,n=n,o=o,js=js+(JS[k[0]] if k else ""),wait=wait)
PPL=PPL.replace("[[48,6.5],[54,7.5],[60,6.5]]","[[78,7.2],[82,8.2],[86,7.2]]")
S["B2"]=TOR("330-6*T","0")+CARX(70,-1.8,20)+L(("cx-9-1.5*T","cy+1.0","cz+1.2"),("cx+40","cy+8","cz"),62)
S["C2"]=TOR("330-6*T","0")+CARX(110,-1.8,14,-5.5)+L(("70","7","-9"),("88","1.5","3"),58)
S["D2"]="if(!window.__CYE&&T>0){window.__CYE=1;W7.cyEnd(true);}W7.WX.rain=Math.max(0,0.8-0.35*T);"+TOR("300","0")+L(("-40+3*T","1.8","0"),("200","60","0"),58)
for k in ("B1","C1","D1"): JS[k]=JS[k]
JS.update({"B2":HY+PPL,"C2":HY+PPL,"D2":HY+PPL})
PPL2=PPL.replace("[[78,7.2],[82,8.2],[86,7.2]]","[[90,7.2],[93.5,8.0],[97,7.2]]")
S["A9"]=TOR("320-6*T","0")+L(("-40+12*T","1.6+0.8*T","0"),("200","58","0"),58)
S["C3"]=TOR("330-6*T","0")+CARX(114,-1.8,14,-5.5)+L(("78","5.5","-11"),("95","1.2","3"),56)
S["D3"]="if(!window.__CYE&&T>0){window.__CYE=1;W7.cyEnd(true);W7.CY.fade=3.2;}W7.WX.rain=Math.max(0,0.8-0.4*T);"+TOR("300","0")+L(("-40+3*T","1.8","0"),("200","60+4*T","0"),58)
JS.update({"A9":HY+PPL,"C3":HY+PPL2,"D3":HY+PPL})
S["C4"]=TOR("330-6*T","0")+CARX(114,-1.8,14,-5.5)+L(("80","5.0","-13"),("93","1.0","2"),58)
JS["C4"]=HY+PPL2
S["C5"]=TOR("330-6*T","0")+CARX(114,-1.8,14,-5.5)+L(("72","5.0","-12"),("96","1.0","-3"),62)
JS["C5"]=HY+PPL2
S["C6"]=TOR("330-6*T","0")+CARX(114,-1.8,14,-5.5)+L(("90","2.6","17"),("97","0.8","-2"),60)
JS["C6"]=HY+PPL2
S["C7"]=TOR("330-6*T","0")+CARX(114,-1.8,14,-5.5)+L(("78","5.5","-11"),("96","1.2","-3"),60)
JS["C7"]=HY+PPL2
S["C8"]=TOR("330-6*T","0")+CARX(114,-1.8,14,-5.5)+L(("95.5","3.0","-15"),("95.5","1.6","4"),60)
JS["C8"]=HY+PPL2
S["C9"]=TOR("330-6*T","0")+CARX(114,-1.8,14,-5.5)+L(("95.5","2.2","-7"),("95.5","1.9","4"),70)
JS["C9"]=HY+PPL2
