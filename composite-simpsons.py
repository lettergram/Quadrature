from __future__ import division
import math
 
def simpson(f, a, b, n):
    """
    Approximates the definite integral of f from a to b by
    the composite Simpson's rule, using n subintervals
    Courtiousy of wikipedia
    """
    h = (b - a) / n
    s = f(a) + f(b)
 
    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)
 
    return s * h / 3
 
print simpson(lambda x:math.sin(x), 0.0, math.pi, 120)
