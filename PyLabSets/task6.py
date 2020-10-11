n = int(input("N = "))
mult_set = set()
for i in range(1, n + 1):
  if n % i == 0:
    mult_set.add(str(i) + "*" + str(n // i))
print("Симметричные представления разные:\n", mult_set)
l = list(mult_set)
for i in range(len(l)):
  a = l[i].split("*")
  for j in range(i + 1, len(l)):
    b = l[j].split("*")
    if a[0] == b[1] and a[1] == b[0]:
      mult_set.discard(l[j])
print("Симметричные представления одинаковые:\n", mult_set)
