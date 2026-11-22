import sys,json; sys.path.insert(0,'/root/cap')
exec(open('/root/cap/jrec.py').read().split('shots=[')[0])
x,z=-39.65,-3332.47
V="const J=window.__JET;J.visible=true;const x=%f-185+80*T;J.position.set(x,150,%f+38);J.rotation.set(0,Math.PI/2,0);J.rotation.z=0.22;return {p:[x-36,153,%f+38+7],t:[x+22,147,%f+34],fov:60};"%(x,z,z,z)
run([J("warm","return {p:[0,60,300],t:[0,20,0],fov:60};"),J("jet2_volC",V,n=52,w=6000)],'/root/w/jf',w=1080,h=1920)
