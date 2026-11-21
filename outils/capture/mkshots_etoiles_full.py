import sys
sys.argv=['s2.py','x','0']
exec(open('/root/cap/s2.py').read().split("sel=sys.argv")[0])
S["tours"]="window.__fxBoost=0;const p=[112,3+8*T,112],t=[40,120+6*T,-10];ST(0,0.2,1.6,-0.36,1.0,1,p,t,700,650);return {p:p,t:t,fov:62};"
S["eau"]=sh("[-760-6*T,1.3,430]","[-1150,35,330]",60,[(0,0.0,1.3,0.33,0.42,-1)])
S["toit"]=sh("[40-3*T,186,40-3*T]","[260,110,330]",62,[(0,0.0,1.3,-0.33,0.3,1)])
S["mont"]=sh("[0+8*T,320,-1950+6*T]","[0,120,-200]",60,[(0,0.1,1.3,0.2,0.2,-1),(1,0.35,1.2,-0.15,0.3,-1)])
N={"tours":65,"eau":37,"toit":37,"mont":50}
names={k:"etoiles_%s_nuit"%k for k in N}
shots=[shot(names[k],S[k],dayT=840,n=n,wait=2500,js=notraf,pre=STAR) for k,n in N.items()]
print(run(shots,'/root/cap/s2f',w=1080,h=1920,wait=False))
