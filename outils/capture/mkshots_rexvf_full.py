from rex import *
SH=[("rexA",polp(1.0,0.97,"60.5-1.0*T",9,23,68),78),
    ("rexB",PIN(1.3)+rel("48","-18","1.2+12*T","0","0","8+13*T",60),52),
    ("rexC",PIN(1.6)+rel("6","-60","7","6","0","16",60),52),
    ("rexD",polp(1.0,1.34,"59-0.8*T",5,20,72),62)]
sh=[mk("w",SH[0][1],wait=3000)]+[mk(k,b,n=n,wait=3000) for k,b,n in SH]
print(run(sh,"/root/w/m1/full",w=1080,h=1920,ev="window.__zonesPretes"))
