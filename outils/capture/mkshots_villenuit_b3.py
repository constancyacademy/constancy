exec(open('/home/claude/rushes/outils/capture/mkshots_villenuit_b2.py').read())
# villenuit_b3 (24/11 0h30, COMMANDE de l'expert du 24/11 0h10) · gens de près la nuit (guinguettes de la plage ouest : clients et danseurs, montrés quand le joueur est à moins de 170 m, forcés visibles ici) · street workout refilmé plus haut
GV="{const W8=window.__W();W8.GUING.people.forEach(h=>{if(!h.__gv&&Math.abs(h.position.x+422)<40){h.__gv=1;Object.defineProperty(h,'visible',{configurable:true,get:()=>true,set:()=>{}});if(h.userData.cup){const c=h.userData.cup;Object.defineProperty(c,'visible',{configurable:true,get:()=>true,set:()=>{}});}}});}"
def GL(p,t,fov=58): return GV+NOLIFE+L(p,t,fov)
# guinguette (-422 ; 80) et (-422 ; 252) : plancher x -414..-430, z ±5.5 ; la ville est vers +x, la mer vers -x
for zc,nm in ((80,"A"),(252,"B"),(-232,"C")):
  S[nm+"1"]=GL(("-433",1.7,"%d-7"%zc),("-418","1.4","%d+2"%zc))
  S[nm+"2"]=GL(("-410","1.8","%d+9"%zc),("-424","1.3","%d"%zc))
  S[nm+"3"]=GL(("-424","6","%d+14"%zc),("-422","0.5","%d"%zc))
  S[nm+"4"]=GL(("-436","2.2","%d+6"%zc),("-412","2.0","%d-2"%zc))
# street workout (-418 ; -205), tapis noir x -426..-410, z -211..-199
S["H1"]=NOLIFE+L(("-424","6","-190"),("-418","0.6","-204"),58)
S["H2"]=NOLIFE+L(("-432","6.5","-205"),("-417","0.4","-205"),58)
S["H3"]=NOLIFE+L(("-405","6","-196"),("-419","0.6","-205"),58)
S["H4"]=NOLIFE+L(("-421","5.5","-218"),("-418","0.8","-204"),58)
S["H5"]=NOLIFE+L(("-412","2.0","-196"),("-424","1.4","-206"),58)
S["H6"]=NOLIFE+L(("-428","5","-196"),("-414","0.6","-207"),58)
S["A5"]=GL(("-432+1.2*T","1.9","88"),("-414","2.2","78"))
S["A6"]=GL(("-433","1.8","72+2*T"),("-416","1.7","81+2*T"))
S["A7"]=GL(("-430","1.9","90-1.5*T"),("-414","2.4","80-1.5*T"),56)
S["H7"]=NOLIFE+L(("-434","6","-208+1.2*T"),("-419","0.6","-207+1.2*T"),58)
S["H8"]=NOLIFE+L(("-433+0.8*T","5.5","-201"),("-419","0.4","-207"),58)
S["H9"]=NOLIFE+L(("-435","6","-211+0.8*T"),("-421","0.6","-210+0.8*T"),58)
S["H10"]=NOLIFE+L(("-436","6.5","-214+1.0*T"),("-423","0.6","-206+1.0*T"),58)
S["H11"]=NOLIFE+L(("-433.5","5.5","-209-0.8*T"),("-420","0.8","-209-0.8*T"),56)
S["H12"]=NOLIFE+L(("-435.5+1.0*T","6.2-0.4*T","-211"),("-421","0.6","-210"),58)
