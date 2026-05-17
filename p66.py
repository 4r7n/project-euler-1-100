from sympy import *
from sympy.solvers.diophantine.diophantine import diop_DN


x, y, t = symbols('x y t')


def f(D):
    return diop_DN(D, 1)[0][1]


M = [0, 0]

for i in range(1, 1000):

    if pow(i, 0.5).is_integer():
        continue

    Dx = f(i)

    if Dx > M[0]:
        M = [Dx, i]

print(M[1])