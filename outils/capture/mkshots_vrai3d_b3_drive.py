exec(open('/root/w/s/m4b2_lib.py').read())
XO=78.0
DRIVE=carjs(XO+50,16,LZ4)+"return {p:[cx-0.5,1.15,%f-5.6],t:[cx+1.2,0.5,%f],fov:55};"%(LZ4,LZ4)
sh=[S_("m4f_drive",DRIVE,46,pre=place2(XO))]
print(run(sh,'/root/w/m4f2',w=1080,h=1920,wait=False))
