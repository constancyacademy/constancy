exec(open('/root/w/s/m4b2_lib.py').read())
O=orbit(-1.25,2.35,1.6)
# rise: car passes the camera at street level, then camera climbs above the roofs
RISE=carjs(X0-16,18,LZ4)+"const u=Math.max(0,T-0.55);const y=1.0+70*Math.pow(Math.min(1,u/1.0),1.7);return {p:[%f+2+6*T,y,%f-4.5],t:[%f+14+10*T,0.9+y*0.55,%f+1],fov:60};"%(X0,LZ4,X0,LZ4)
DRIVE=carjs(X0+18,16,LZ4)+"return {p:[cx-1.5,1.05,%f-4.2],t:[cx+2.2,0.15,%f],fov:55};"%(LZ4,LZ4)
sh=[shot("warm","return {p:[0,60,300],t:[0,20,0],fov:60};",dayT=840),
 S_("m4b_orbit",O,62),
 S_("m4b_rise",RISE,50),
 S_("m4b_drive",DRIVE,44),
]
print(run(sh,'/root/w/m4b',w=1080,h=1920,wait=False))
