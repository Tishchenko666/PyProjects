size = int(input("N = "))
l = list(range(1, size + 1))
print(l)
l_sum = 0
for i in range(size):
  if i == 0:
    l.append(l[0])
  else:
    l_sum += l[i - 1]
    l.append(l_sum)
del l[0:size]
print(l)