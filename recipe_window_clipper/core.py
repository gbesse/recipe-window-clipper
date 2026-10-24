from fractions import Fraction as F
from .common import unique_ids

def exact(x):
 if isinstance(x,bool)or not isinstance(x,(str,int,float))or len(str(x))>50:raise ValueError('rational')
 v=F(str(x))
 if abs(v)>10**12:raise ValueError('bounds')
 return v
def clip(poly,constraints):
 for c in constraints:
  a,b,z=c;out=[]
  if not poly:return []
  for p,q in zip(poly,poly[1:]+poly[:1]):
   fp=a*p[0]+b*p[1]-z;fq=a*q[0]+b*q[1]-z
   if fp<=0:out.append(p)
   if (fp<0 and fq>0)or(fp>0 and fq<0):
    u=fp/(fp-fq);out.append((p[0]+u*(q[0]-p[0]),p[1]+u*(q[1]-p[1])))
  poly=list(dict.fromkeys(out))
 return poly
def run(data):
 box=data['bounds'];x0,x1=map(exact,box['x']);y0,y1=map(exact,box['y'])
 if x0>x1 or y0>y1:raise ValueError('box')
 cs=data['constraints'];unique_ids(cs)
 if len(cs)>30:raise ValueError('constraints')
 parsed=[(exact(c['a']),exact(c['b']),exact(c['max']))for c in cs];base=list(dict.fromkeys([(x0,y0),(x1,y0),(x1,y1),(x0,y1)]));poly=clip(base,parsed);core=[]
 if not poly:
  core=list(range(len(cs)))
  for i in core[:]:
   if not clip(base,[parsed[j]for j in core if j!=i]):core.remove(i)
 area=abs(sum(p[0]*q[1]-q[0]*p[1]for p,q in zip(poly,poly[1:]+poly[:1])))/2 if poly else F(0)
 return {'feasible':bool(poly),'vertices':[[str(x),str(y)]for x,y in poly],'area':str(area),'infeasible_core':[cs[i]['id']for i in core],'fixed_domain_box':{'x':[str(x0),str(x1)],'y':[str(y0),str(y1)]},'model':'exact_rational_halfplane_intersection_in_fixed_box'}
