exec(open('/root/w/vi/b2k.py').read().split('\nnames=')[0])
S["K8"]=L(V("1.5-5*T",2.4,-2.5),V("-0.5-7*T",3.0,7),66)
S["K9"]=L(V("1.5-5*T",2.3,-2.5),V("-0.5-7*T",2.7,7),70)
for k in ("K8","K9"): HL[k]=0.22
names=sys.argv[2].split(',')
offs=[float(x) for x in sys.argv[3].split(',')]
shots=[MKI("x",S["W1"],hl=0.3)]; shots[0]["fps"]=60; shots[0]["n"]=1
for k in names:
  for o in offs:
    sh=MKI(k+"o%02d"%int(round(o*10)),S[k],o=o,hl=HL.get(k,0.3),ext=EXT.get(k,0)); sh["fps"]=60; sh["n"]=1; shots.append(sh)
print(run(shots,sys.argv[1],w=1080,h=1920))
