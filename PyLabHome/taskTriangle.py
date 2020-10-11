"""Даны три произвольных числа a, b, c. Могут ли они быть длинами сторон некоторого треугольника?
Если да, найти его углы и определить тип (остроугольный, тупоугольный, прямоугольный)."""

import math
import random

a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
  print(a, b, c, "- длинны сторон триугольника")
  c2 = c ** 2
  a2 = a ** 2
  b2 = b ** 2
  if c2 == a2 + b2:
    print("Этот триугольник прямоугольный")
  elif c2 < a2 + b2:
    print("Этот триугольник остроугольный")
  else:
    print("Этот триугольник тупоугольный")
  alfa = round(math.acos((b2 + c2 - a2) / (2 * b * c)) * 180 / math.pi, 1)
  beta = round(math.acos((c2 + a2 - b2) / (2 * a * c)) * 180 / math.pi, 1)
  gamma = round(math.acos((a2 + b2 - c2) / (2 * a * b)) * 180 / math.pi, 1)
  print("Значения углов приближены к целым числам.")
  print(alfa, beta, gamma, "- углы напротив сторон a, b, c")
else:
  print(a, b, c, "- не длинны сторон триугольника")
