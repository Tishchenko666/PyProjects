from random import uniform
from math import log, sin

x = uniform(-2.0, 2.0)
if x < -0.5:
  y = round(log(-2 * x), 3)
elif -0.5 <= x <= 1:
  y = 0
elif x > 1:
  y = round(sin(1 - x), 3)
print("При х =", round(x, 3), "у =", y)
