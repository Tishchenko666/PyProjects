from random import randint

s = set()
s1 = set()
while len(s) != 10:
  s.add(randint(1, 101))
print("Множество =", s)