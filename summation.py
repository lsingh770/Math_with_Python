# -*- coding: utf-8 -*-
"""
Summations
------------------
perfrom summation of 2i where 'i' iterates from 1 to 5

range() func in Python is end exclusive
"""

from sympy import *
summation = sum(2*i for i in range(1, 6))
print(summation)

""" 
Perform summation for '10x' where values of x are provided
"""

x = [1, 4, 6, 2]
n = len(x)
summation1 = sum(10*i for i in range(0, n))
print(summation1)

"""
Summation using sympy
"""

i, n = symbols('i n')

# iterare each element i from 1 to n
# then multiply and sum
summation2 = Sum(2*i, (i, 1, n))

# specify n as 5,
# iterating the numbers 1 through 5
upto_5 = summation2.subs(n, 5)
print(upto_5.doit())
