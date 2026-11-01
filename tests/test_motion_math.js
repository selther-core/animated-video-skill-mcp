'use strict';
const assert=require('assert');
const fs=require('fs');const path=require('path');
const dir=path.join(__dirname,'../.agents/skills/cinematic-narrative-video/examples');
assert.ok(fs.readFileSync(path.join(dir,'contact-light-study.html'),'utf8').includes(fs.readFileSync(path.join(dir,'contact-physics.js'),'utf8')), 'Standalone demo must embed current helper.');
const {solveTwoBone,apply,inverse,multiply}=require('../.agents/skills/cinematic-narrative-video/examples/contact-physics.js');
const near=(a,b,tol=1e-7)=>assert.ok(Math.abs(a-b)<tol,`${a} != ${b}`);
const d=(a,b)=>Math.hypot(a[0]-b[0],a[1]-b[1]);
for(const target of [[15,0],[5,8],[0,0],[10,10],[200,0]]){
 const p=solveTwoBone([0,0],target,10,10);near(d([0,0],p.joint),10);near(d(p.joint,p.end),10);assert.equal(p.reachable,d([0,0],target)<=20);if(p.reachable && d([0,0],target)>0)near(p.error,0);
}
assert.equal(solveTwoBone([0,0],[1,0],10,4).reachable,false);
const a=[1.2,0.2,-.1,1.4,28,-31],b=[1,0,0,1,4,7],p=[7,9];const w=apply(a,p),back=apply(inverse(a),w);near(back[0],p[0]);near(back[1],p[1]);const m=apply(multiply(a,b),p),n=apply(a,apply(b,p));near(m[0],n[0]);near(m[1],n[1]);
assert.throws(()=>inverse([0,0,0,0,0,0]));assert.throws(()=>solveTwoBone([0,0],[1,2],0,1));
console.log('Motion math tests passed.');
