"""Первое и единственное. Найти первое (и единственное) натуральное число,
которое в пять раз меньше суммы предшествующих ему натуральных чисел."""

num_sum = 1
i = 2
while True:
  if num_sum // i == 5:
    print("Искомое число =", i)
    break
  else:
    num_sum += i
    i += 1