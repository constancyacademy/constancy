exec(open('/root/w/s/m4b2_lib.py').read())
RISE=carjs(X0-6,22,LZ4)+"const u=Math.max(0,T-0.55);const y=1.0+70*Math.pow(Math.min(1,u/1.0),1.7);return {p:[%f+2+6*T,y,%f-4.5],t:[%f+14+10*T,0.9+y*0.55,%f+1],fov:60};"%(X0,LZ4,X0,LZ4)
DRIVE=carjs(X0+18,16,LZ4)+"return {p:[cx-0.5,1.15,%f-5.6],t:[cx+1.2,-0.35,%f],fov:55};"%(LZ4,LZ4)
sh=[shot("warm","return {p:[0,60,300],t:[0,20,0],fov:60};",dayT=840),S_("m4c_rise",RISE,50),S_("m4c_drive",DRIVE,40)]
print(run(sh,'/root/w/m4c',w=1080,h=1920,wait=False))
