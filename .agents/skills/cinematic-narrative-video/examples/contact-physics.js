/* Original reusable 2D motion helpers. Coordinates must use one consistent space. */
(function (root) {
  'use strict';
  function solveTwoBone(start, desired, l1, l2, bend = 1) {
    const finite = p => Array.isArray(p) && p.length === 2 && p.every(Number.isFinite);
    if (!finite(start) || !finite(desired) || !Number.isFinite(l1) || !Number.isFinite(l2) || l1 <= 0 || l2 <= 0 || ![1,-1].includes(bend)) throw Error('Invalid two-bone inputs');
    let dx=desired[0]-start[0], dy=desired[1]-start[1], d=Math.hypot(dx,dy);
    const min=Math.abs(l1-l2), max=l1+l2, reachable=d>=min-1e-9 && d<=max+1e-9;
    const ux=d>1e-9?dx/d:1, uy=d>1e-9?dy/d:0;
    const safe=Math.max(1e-9,Math.min(max,Math.max(min,d)));
    const a=(l1*l1-l2*l2+safe*safe)/(2*safe), h=Math.sqrt(Math.max(0,l1*l1-a*a));
    const joint=[start[0]+a*ux-bend*h*uy,start[1]+a*uy+bend*h*ux];
    const end=[start[0]+safe*ux,start[1]+safe*uy];
    return {joint,end,reachable,error:Math.hypot(end[0]-desired[0],end[1]-desired[1])};
  }
  function apply(m,p){ return [m[0]*p[0]+m[2]*p[1]+m[4],m[1]*p[0]+m[3]*p[1]+m[5]]; }
  function inverse(m){ const [a,b,c,d,e,f]=m, det=a*d-b*c; if (!Number.isFinite(det)||Math.abs(det)<1e-12) throw Error('Singular transform'); return [d/det,-b/det,-c/det,a/det,(c*f-d*e)/det,(b*e-a*f)/det]; }
  function multiply(m,n){ const [a,b,c,d,e,f]=m,[g,h,i,j,k,l]=n;return [a*g+c*h,b*g+d*h,a*i+c*j,b*i+d*j,a*k+c*l+e,b*k+d*l+f]; }
  const api={solveTwoBone,apply,inverse,multiply};
  if(typeof module!=='undefined' && module.exports) module.exports=api;
  root.MotionMath=api;
})(typeof globalThis!=='undefined'?globalThis:this);
