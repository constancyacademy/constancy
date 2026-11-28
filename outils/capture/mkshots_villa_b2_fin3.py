exec(open('/root/w/vi/b2fin2.py').read().split('\nnames=')[0])
S["H2"]=L(V("0-5*T",2.4,-2.5),V("-2.5-6.5*T",3.6,7),66); HL["H2"]=0.22; F["H2"]=80
names=sys.argv[2].split(',')
shots=[MKI("x",S["W1"],hl=0.3)]; shots[0]["fps"]=60; shots[0]["n"]=1
for k in names:
  sh=MKI(k,S[k],hl=HL.get(k,0.3),ext=EXT.get(k,0)); sh["fps"]=60; sh["n"]=F[k]; shots.append(sh)
print(run(shots,sys.argv[1],w=1080,h=1920))
