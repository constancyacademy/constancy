exec(open('/root/w/vi/b2m.py').read().split('\nnames=')[0])
S["F1"]=AQ(162,-14,46,9,1.8,0.6,3.0,50,tp=0.3); F["F1"]=105
S["F2"]=L(V("1.5-5*(T-0.4)",2.4,-2.5),V("-0.5-7*(T-0.4)",3.0,7),66); HL["F2"]=0.22; F["F2"]=102
S["F3"]=L(V("-14+9*T",2.0,18),V("-10+9*T",0.5,6),60); HL["F3"]=0.25; F["F3"]=90
S["F5"]=ORB2(94,12,38,13,3.5,68); F["F5"]=120
names=sys.argv[2].split(',')
shots=[MKI("x",S["W1"],hl=0.3)]; shots[0]["fps"]=60; shots[0]["n"]=1
for k in names:
  sh=MKI(k,S[k],hl=HL.get(k,0.3),ext=EXT.get(k,0)); sh["fps"]=60; sh["n"]=F[k]; shots.append(sh)
print(run(shots,sys.argv[1],w=1080,h=1920))
