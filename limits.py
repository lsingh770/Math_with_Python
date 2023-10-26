# -*- coding: utf-8 -*-
"""
calculate limits
"""

from sympy import *
# %%
x = symbols('x')
f = 1 / x
result = limit(f, x, oo)

print(result)  # 0
# %%
# Calculate Euler's number with limits

n = symbols('n')
f = (1 + (1/n))**n
result = limit(f, n, oo)

print(result)   # E
print(result.evalf())  # 2.71828182845905
# %%
