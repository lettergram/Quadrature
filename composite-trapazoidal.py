import math

def comp_trap(f, a, b, n):
    h = (b - a) / n
    sum = f(a) / 2
    for i in xrange(1, n):
        sum += 2 * f(a + i * h)
    return sum * h / 2


print comp_trap(lambda x:math.sin(x), 0.0, math.pi, 120)

