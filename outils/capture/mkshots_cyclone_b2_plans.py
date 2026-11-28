exec(open('/home/claude/rushes/outils/capture/mkshots_cyclone_b1_plans.py').read())
DTS={}
D=360
S["A"]=TOR("150-4*T","0")+L(("-40+12*T","1.6+0.6*T","0"),("200","55","0"),62); JS["A"]=HY; DTS["A"]=D
S["B"]=TOR("210-4*T","0")+CARX(70,-1.8,20)+L(("cx-9-1.5*T","cy+1.0","cz+1.2"),("cx+40","cy+8","cz"),62); JS["B"]=HY; DTS["B"]=D
RUN=("{const W9=window.__W();const car=window.__HY;car.position.set(96,W9.GH(96,-1.8),-1.8);car.rotation.order='YXZ';car.rotation.y=-1.5708;"
     "const st=[[92,5.2,0.0],[95.2,5.8,0.25],[98.5,5.0,0.5]];(W9.CY.ppl||[]).forEach((q,k)=>{const s=st[k];if(!s||!q.m)return;q.m.position.set(s[0],W9.GH(s[0],s[1])+0.02,s[1]);q.m.visible=true;if(q.b)q.b.position.set(s[0],W9.GH(s[0],s[1]),s[1]);try{W9.setClip(q.m,'Sprint_Loop',1.0,0.1);}catch(e){}});window.__RUN=st;}")
RUNCAM=("{const W8=window.__W();const st=window.__RUN;const dx=95.6,dz=-0.4;(W8.CY.ppl||[]).forEach((q,k)=>{const s=st[k];if(!s||!q.m)return;const t=Math.max(0,T-s[2]);const L0=Math.hypot(dx-s[0],dz-s[1]);const d=Math.min(L0,5.2*t);const x=s[0]+(dx-s[0])*d/L0,z=s[1]+(dz-s[1])*d/L0;"
        "q.m.position.set(x,W8.GH(x,z)+0.02,z);q.m.rotation.y=Math.atan2(dx-s[0],dz-s[1]);if(q.b)q.b.position.set(x,W8.GH(x,z),z);const gone=d>=L0-0.9;q.m.visible=!gone;if(q.b)q.b.visible=!gone;});}")
S["C"]=TOR("210","0")+RUNCAM+L(("84+2*T","3.2","15"),("96","1.0","0"),58); JS["C"]=HY+RUN; DTS["C"]=D
S["C2"]=TOR("210","0")+RUNCAM+L(("103-1.5*T","2.4","12"),("94","1.2","0"),60); JS["C2"]=HY+RUN; DTS["C2"]=D
DIS="if(!window.__CYE&&T>0){window.__CYE=1;W7.cyEnd(true);}if(window.__CYE){W7.CY.fade=Math.max(0.01,6-5*T);}W7.WX.rain=Math.max(0,0.8-0.5*T);"
S["Dd"]=DIS+TOR("190","40")+L(("20+4*T","24+6*T","-70"),("190","60","40"),58); JS["Dd"]=HY; DTS["Dd"]=D
RUN2=RUN.replace("if(q.b)q.b.position.set(s[0],W9.GH(s[0],s[1]),s[1]);","if(q.b){q.b.visible=false;}")
RUNCAM2=RUNCAM.replace("if(q.b)q.b.position.set(x,W8.GH(x,z),z);","").replace("if(q.b)q.b.visible=!gone;","if(q.b)q.b.visible=false;")
S["C3"]=TOR("210","0")+RUNCAM2+L(("85.5+1.2*T","2.0","2.5"),("97","1.1","1.5"),60); JS["C3"]=HY+RUN2; DTS["C3"]=D
S["C4"]=TOR("210","0")+RUNCAM2+L(("80+1.5*T","3.0","-1"),("97","1.0","3"),56); JS["C4"]=HY+RUN2; DTS["C4"]=D
S["D2"]=DIS+TOR("230","0")+L(("50+3*T","38+5*T","-6"),("230","70","0"),56); JS["D2"]=HY+"window.__HY.visible=false;"; DTS["D2"]=D
JS["A"]=HY+"window.__HY.visible=false;"
S["C5"]=TOR("210","0")+RUNCAM2+L(("99.5-1.2*T","2.4","-13"),("96","1.3","2"),56); JS["C5"]=HY+RUN2; DTS["C5"]=D
S["D3"]=DIS.replace("6-5*T","6-4.2*T")+TOR("290","0")+L(("50+3*T","38+5*T","-6"),("290","75","0"),56); JS["D3"]=HY+"window.__HY.visible=false;"; DTS["D3"]=D
S["X"]=L(("0","300","300"),("0","0","0"),60)
