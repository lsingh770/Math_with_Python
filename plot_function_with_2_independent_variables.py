# -*- coding: utf-8 -*-
''' 
    f(x,y) = 2x + 3y
'''

from sympy import *
from sympy.plotting import plot3d

x, y = symbols('x y')
f = 2*x + 3*y
plot3d(f)
