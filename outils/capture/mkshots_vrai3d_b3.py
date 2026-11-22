exec(open('/root/w/s/m4b2_lib.py').read())
XO=78.0; XR=100.0
O=orbit2(XO,-3.6,-0.3,2.0)
RISE="const u=Math.max(0,T-0.35);const k=Math.min(1,u/1.1);const y=1.0+110*Math.pow(k,1.6);const ty=(0.9+y*0.5)*(1-k)+(y*0.85)*k;return {p:[%f+2+5*T,y,%f-4.5],t:[%f+20+100*k,ty,%f+1],fov:60};"%(XR,LZ4,XR,LZ4)
DRIVE=carjs(XO+18,16,LZ4)+"return {p:[cx-0.5,1.15,%f-5.6],t:[cx+1.2,-0.1,%f],fov:55};"%(LZ4,LZ4)
sh=[shot("warm","return {p:[0,60,300],t:[0,20,0],fov:60};",dayT=840),
 S_("m4d_orbit",O,62,pre=place2(XO)),
 S_("m4d_rise",RISE,52,pre=place2(XO)+"{if(window.__PC)window.__PC.forEach(g=>g.visible=false);}"),
 S_("m4d_drive",DRIVE,42,pre=place2(XO)),
]
print(run(sh,'/root/w/m4d',w=1080,h=1920,wait=False))
