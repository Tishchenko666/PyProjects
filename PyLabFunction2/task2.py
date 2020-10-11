from random import randint
from math import sqrt


def full_square(l):
  sq = []
  for i in range(len(l)):
    if int(sqrt(l[i])) == float(sqrt(l[i])):
      sq.append(l[i])
  if len(sq) > 0:
    print("Полные квадраты = ", sq)
  else:
    print("В списке нет полных квадратов")


n = int(input("Длинна списка: "))
nums = [randint(1, 1000) for i in range(n)]
print("Список чисел =", nums)
full_square(nums)
