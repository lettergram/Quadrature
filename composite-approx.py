import math

def comp_midpoint(f, a, b, n):
  sum = 0
  h = (b - a) / n
  x = h/2
  for i in range(n):
    sum += f(x) * h
    x += h
  return sum

def comp_simpson(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)
    return s * h / 3

def comp_trap(f, a, b, n):
    h = (b - a) / n
    sum = f(a) / 2
    for i in xrange(1, n):
        sum += 2 * f(a + i * h)
    return sum * h / 2

f = open('comp-approx.txt', 'w')
f.write('Number of Iterations, Composite Trapazoid x^3, Composite Midpoint x^3, Composite Simpson x^3, Composite Trapazoid sin(x), Composite Midpoint sin(x), Composite Simpson sin(x)\n')
for n in xrange(1, 500):
    str = "%d" % n + ","
    str += "%.9f" % comp_trap(lambda x:x*x*x, 0.0, 5, n) + ","
    str += "%.9f" % comp_midpoint(lambda x:x*x*x, 0.0, 5, n) + ","
    str += "%.9f" % comp_simpson(lambda x:x*x*x, 0.0, 5, n) + ","
    str += "%.9f" % comp_trap(lambda x:math.sin(x), 0.0, math.pi / 2, n) + ","
    str += "%.9f" % comp_midpoint(lambda x:math.sin(x), 0.0, math.pi / 2, n) + ","
    str += "%.9f" % comp_simpson(lambda x:math.sin(x), 0.0, math.pi / 2, n) + "\n"
    f.write(str)
