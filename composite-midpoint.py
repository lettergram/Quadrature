import math 

def comp_midpoint(f, a, b, n):
  sum = 0
  h = (b - a) / n
  x = h/2
  for i in range(n):
    sum += f(x) * h
    x += h
  return sum

print comp_midpoint(lambda x:math.sin(x), 0.0, math.pi / 2, 120)
