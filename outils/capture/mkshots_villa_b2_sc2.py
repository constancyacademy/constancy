exec(open('/root/w/vi/b2.py').read().split('\nnames=')[0])
S["K1"]=L(V("-10+6*T",2.0,-2),V("-8+6*T",2.1,7),66)
S["K2"]=L(V("-10+6*T",2.0,0),V("-8+6*T",2.1,7),70)
S["K3"]=L(V("-2-6*T",2.0,-2),V("-4-6*T",2.1,7),66)
S["K4"]=L(V("-10+6*T",2.2,-4),V("-4+6*T",1.8,7),66)
S["Q7"]=ORB2(94,12,36,11,2.5,70)
S["Q8"]=ORB2(94,12,38,13,3.5,68)
for k in ("K1","K2","K3","K4"): HL[k]=0.22
names=sys.argv[2].split(',')
offs=[float(x) for x in sys.argv[3].split(',')]
shots=[MKI("x",S["W1"],hl=0.3)]; shots[0]["fps"]=60; shots[0]["n"]=1
for k in names:
  for o in offs:
    sh=MKI(k+"o%02d"%int(round(o*10)),S[k],o=o,hl=HL.get(k,0.3),ext=EXT.get(k,0)); sh["fps"]=60; sh["n"]=1; shots.append(sh)
print(run(shots,sys.argv[1],w=1080,h=1920))
