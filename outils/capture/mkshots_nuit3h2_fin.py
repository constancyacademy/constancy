import sys,json; sys.path.insert(0,'/root/cap')
exec(open('/root/cap/n3rec3.py').read().split('shots=[')[0])
BD="const a=0.4+0.18*T,r=22-9*T,h=11-6.5*T;return {p:[132+r*Math.cos(a),17+h,188+r*Math.sin(a)],t:[132,18.3,188],fov:60};"
AO="const a=0.9+0.35*T;return {p:[84+11*Math.cos(a),69+4.5,28+11*Math.sin(a)],t:[84,70.2,28],fov:60};"
C3="const a=1.6+0.25*T;return {p:[-35+9*Math.cos(a),27,-203+9*Math.sin(a)],t:[-35,25.3,-203],fov:60};"
S2="return {p:[250-55*T,40,330],t:[60-30*T,55,-20],fov:60};"
def F(name,body,n,toff=0):
  s=S(name,body,n=n,toff=toff,w=2500); return s
shots=[S("warm","return {p:[0,60,300],t:[0,20,0],fov:60};"),
 F("n3_BD",BD,44), F("n3_BDpre",BD,15,toff=-0.5), F("n3_AO",AO,44), F("n3_C3",C3,44), F("n3_S2",S2,44)]
run(shots,'/root/w/n3f',w=1080,h=1920)
