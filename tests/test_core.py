import unittest
from fractions import Fraction as F
from recipe_window_clipper import run
class Tests(unittest.TestCase):
 def test_known_triangle_area(self):
  r=run({'bounds':{'x':[0,4],'y':[0,4]},'constraints':[{'id':'c','a':1,'b':1,'max':4}]});self.assertEqual(F(r['area']),8);self.assertEqual(set(map(tuple,r['vertices'])),{('0','0'),('4','0'),('0','4')})
 def test_fractional_vertices_are_exact(self):
  r=run({'bounds':{'x':[0,1],'y':[0,1]},'constraints':[{'id':'c','a':3,'b':3,'max':1}]});self.assertEqual(F(r['area']),F(1,18));self.assertIn(['1/3','0'],r['vertices'])
 def test_irreducible_core_preserves_fixed_box(self):
  cs=[{'id':'left','a':1,'b':0,'max':0},{'id':'right','a':-1,'b':0,'max':-1},{'id':'redundant','a':0,'b':1,'max':9}];d={'bounds':{'x':[-2,2],'y':[-2,2]},'constraints':cs};r=run(d);self.assertFalse(r['feasible']);self.assertEqual(set(r['infeasible_core']),{'left','right'})
  for name in r['infeasible_core']:self.assertTrue(run({**d,'constraints':[c for c in cs if c['id']in r['infeasible_core']and c['id']!=name]})['feasible'])
 def test_boundary_point_is_feasible(self):
  r=run({'bounds':{'x':[1,1],'y':[2,2]},'constraints':[{'id':'c','a':1,'b':1,'max':3}]});self.assertTrue(r['feasible']);self.assertEqual(r['vertices'],[['1','2']]);self.assertEqual(r['area'],'0')
 def test_zero_coefficient_contradiction(self):self.assertFalse(run({'bounds':{'x':[0,1],'y':[0,1]},'constraints':[{'id':'impossible','a':0,'b':0,'max':-1}]})['feasible'])

class ExponentBounds(unittest.TestCase):
 def test_extreme_exponent_refused_before_fraction_allocation(self):
  from recipe_window_clipper.core import exact
  for raw in ('1e1000000000','1e-1000000000'):
   with self.assertRaises(ValueError):exact(raw)
  self.assertEqual(exact('1e-3'),F(1,1000))
