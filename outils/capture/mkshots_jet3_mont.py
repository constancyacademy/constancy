import sys,json; sys.path.insert(0,'/root/cap')
exec(open('/root/cap/jrec.py').read().split('shots=[')[0])
M="const J=window.__JET;J.visible=true;const z=-1250-235*T;J.position.set(-22+6,98.8,z);J.rotation.set(0,Math.PI,0);J.rotation.z=0.12;return {p:[-22,106,z+36],t:[-22,99,z-190],fov:60};"
sh=[J("warm","return {p:[0,60,300],t:[0,20,0],fov:60};"),J("jet3_montJ",M,n=42,w=9000)]
print(run(sh,'/root/w/jf12',w=1080,h=1920))
