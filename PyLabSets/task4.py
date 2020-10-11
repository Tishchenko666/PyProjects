n = input("Список чисел: ")
s = n.split(" ")
t = set()
for i in range(1, len(s)):
  if i == 1 and int(s[i]) == int(s[i - 1]):
    t.add(s[i])
  elif int(s[i]) == int(s[i - 1]) + int(s[i - 2]):
    t.add(s[i])
k = set(s)
k.difference_update(t)
print("Числа Фибоначчи удалены: ", " ".join(j for j in k))
