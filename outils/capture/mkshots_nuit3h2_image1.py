import sys,json; sys.path.insert(0,'/root/cap')
exec(open('/root/cap/n3rec3.py').read().split('shots=[')[0])
BD="const a=-2.4+0.16*T,r=19.5-5*T,h=10-4.3*T;return {p:[132+r*Math.cos(a),17+h,188+r*Math.sin(a)],t:[132,18.0,188],fov:60};"
shots=[S("warm","return {p:[0,60,300],t:[0,20,0],fov:60};"), S("n3_BF",BD,n=44,w=2500)]
run(shots,'/root/w/n3f',w=1080,h=1920)
