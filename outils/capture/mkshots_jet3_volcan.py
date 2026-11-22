import sys,json; sys.path.insert(0,'/root/cap')
exec(open('/root/cap/jrec.py').read().split('shots=[')[0])
x,z=-39.65,-3332.47
VK="const J=window.__JET;J.visible=true;const zp=%f+165-110*T;const xp=%f+48;const yp=Math.max(45,182-0.95*(zp-(%f)));J.position.set(xp,yp,zp);J.rotation.set(-0.35,Math.PI,0);J.rotation.z=-0.15;return {p:[xp+12,yp+50,zp+34],t:[xp,yp-22,zp-30],fov:60};"%(z,x,z)
sh=[J("warm","return {p:[0,60,300],t:[0,20,0],fov:60};"),J("jet3_volL",VK,n=48,w=6000)]
print(run(sh,'/root/w/jf10',w=1080,h=1920))
