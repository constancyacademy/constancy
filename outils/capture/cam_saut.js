(G)=>{const W=window.__W(),g=W.G;const T=(performance.now()-(window.__T0||performance.now()))/1000;
const E=k=>k<0?0:k>1?1:k*k*(3-2*k);const P=window.__CP;
let ax,ay,az,h;
if(g.para){ if(window.__TJ==null)window.__TJ=T; ax=g.me.x;ay=g.para.alt+1.5;az=g.me.z;h=g.me.h;} else {ax=g.car.x;ay=(g.car.alt||0);az=g.car.z;h=g.car.h;}
let S=window.__CS; if(!S||Math.hypot(ax-S.x,ay-S.y,az-S.z)>60){S=window.__CS={x:ax,y:ay,z:az,h:h};}
const k=P.k||0.3; S.x+=(ax-S.x)*k;S.y+=(ay-S.y)*k;S.z+=(az-S.z)*k;S.h+=(h-S.h)*k;
if(T<(P.skip||0)) return {p:[S.x,S.y+5,S.z],t:[S.x,S.y+500,S.z+1],fov:60};
const TJ=window.__TJ, j=TJ==null?0:E((T-TJ)/(P.jd||0.9)), o=E((T-(P.ot||99))/(P.od||1.2));
const a=(P.a0+T*P.av)*(1-j)+(P.aj+(P.ajv||0)*Math.max(0,T-(TJ||T)))*j+(P.ao||0)*o, d=(P.d0-Math.min(T,2)/2*(P.d0-P.d1))*(1-j)+P.dj*j, hg=P.hg*(1-j)+P.hj*j+(P.ho||0)*o;
const px=S.x-Math.sin(S.h+a)*d, pz=S.z-Math.cos(S.h+a)*d, py=S.y+hg;
const tx=S.x+Math.sin(S.h)*(P.tf||0), tz=S.z+Math.cos(S.h)*(P.tf||0), ty=S.y-(P.td||0)*(1-j)-(P.tdj||0)*j-(P.tdo||0)*o;
if(window.__LOGF)try{console.log('LOG '+T.toFixed(3)+' para='+(!!g.para)+' alt='+(g.para?g.para.alt:g.car.alt).toFixed(1)+' ghost='+(g.ghost?g.ghost.alt.toFixed(1)+' gp='+g.ghost.pitch.toFixed(2):'-'));}catch(e){}
return {p:[px,py,pz],t:[tx,ty,tz],fov:P.fov||60};}
