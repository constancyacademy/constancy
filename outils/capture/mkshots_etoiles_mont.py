import sys
sys.argv=['s2.py','x','0']
exec(open('/root/cap/s2.py').read().split("sel=sys.argv")[0])
S["mont"]=sh("[0+8*T,320,-1950+6*T]","[0,120,-200]",60,[(0,0.05,1.3,0.3,0.07,-1),(1,0.35,1.2,-0.32,0.10,1)])
print(run([shot("etoiles_mont_nuit",S["mont"],dayT=840,n=51,wait=2500,js=notraf,pre=STAR)],'/root/cap/s2m',w=1080,h=1920,wait=False))
