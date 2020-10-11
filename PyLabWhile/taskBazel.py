import math

e_sum = round(math.pi ** 2 / 6, 5)
number_of_term = 0
c_sum = 0
i = 1
while c_sum <= e_sum:
  c_sum = c_sum + (1 / (i ** 2))
  number_of_term += 1
  i += 1
print("Взять слогаемых =", number_of_term)
