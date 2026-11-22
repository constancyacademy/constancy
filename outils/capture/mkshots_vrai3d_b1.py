exec(open('/root/w/s/m4_lib.py').read())
RISE="const k=Math.min(1,T/1.35);const y=1.6+115*Math.pow(k,1.5);return {p:[%f-18+12*T,y,0.0],t:[%f+70,0.6+y*0.45,0.0],fov:60};"%(X0,X0)
HIGH="const a=-0.9+0.35*T;return {p:[28+150*Math.cos(a),130-6*T,-28+150*Math.sin(a)],t:[28,40,-28],fov:60};"
sh=[shot("warm","return {p:[0,60,300],t:[0,20,0],fov:60};",dayT=840),
 S_("m4_orbit",orbit(-0.7,2.3,2.0),61),
 S_("m4_drive",drive(16,"return {p:[cx-2.5,0.6,%f-3.4],t:[cx+2.5,0.9,%f],fov:55};"%(LZ4,LZ4)),40),
 S_("m4_rise",RISE,42),
 S_("m4_high",HIGH,50),
]
print(run(sh,'/root/w/m4f',w=1080,h=1920,wait=False))
