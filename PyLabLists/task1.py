size = int(input("N = "))
an1 = []
for n in range(1, size * 2):
  if n % 2 != 0:
    an1.append(n ** 3)
print("Method of filling 1 =", an1)
an2 = [n ** 3 for n in range(1, size * 2) if n % 2 != 0]
print("Method of filling 2 =", an2)
