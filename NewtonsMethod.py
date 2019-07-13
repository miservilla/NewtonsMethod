from sympy import *

x = Symbol('x')
y = 48 * x * (1 + x)**60 - (1 + x)**60 + 1
newtonsMethod = x-(y / y.diff(x))
print(newtonsMethod)


def runnewtonsmethod(n):
    f = lambdify(x, newtonsMethod)
    n = round(f(n), 6)

    while n != round(f(n), 6):
        return runnewtonsmethod(n)

    return n


print(runnewtonsmethod(1))
