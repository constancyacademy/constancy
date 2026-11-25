exec(open('/home/claude/rushes/outils/capture/mkshots_creature_b2.py').read())
# creature_b3 : ouverture 34 éclairée qui fonce vers le Rex, plan final plus serré
for k,(dp,r0,v,h,fov) in {"P1":("1.40-0.10*T","50",5.5,12,55),"P2":("1.55-0.12*T","50",5.0,10,56),"P3":("1.25+0.10*T","50",5.5,13,55),"P4":("1.40-0.10*T","52",6.5,9,58)}.items():
  S[k]=LC(camA(1.0,dp,"%s-%s*T"%(r0,v),"(%s-1.5*T)"%h,"EYES",0.5,0.44,fov)); LJ[k]=2.2
for k,(r,v,fov) in {"Q1":(52,0.595,82),"Q2":(48,0.60,84),"Q3":(50,0.60,80)}.items():
  S[k]=LC2(camA(1.0,"2.0-0.12*T",r,11,"L_Foot",0.5,v,"(%s+3*T)"%fov)); LJ[k]=1.6
S["Q4"]=LC2(camA(1.0,"2.0-0.12*T",52,11,"L_Foot",0.5,0.595,"(84+3*T)")); LJ["Q4"]=1.6
