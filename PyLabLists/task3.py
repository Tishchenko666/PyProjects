from math import sqrt

f = open("countries.csv", "r")
header = f.readline()

text = f.readlines()
n = len(text)
x = []
y = []
for line in text:
  words = line.split(";")
  x.append(float(words[1]))
  y.append(float(words[3]))
print("x =", x)
print("y =", y)
sum_xy = 0
sum_x_square = 0
sum_y_square = 0
for i in range(n):
  sum_xy += x[i] * y[i]
  sum_x_square += x[i] ** 2
  sum_y_square += y[i] ** 2
r_numerator = n * sum_xy - sum(x) * sum(y)
r_denominator = sqrt((n * sum_x_square - sum(x) ** 2) * (n * sum_y_square - sum(y) ** 2))
r = round(r_numerator / r_denominator, 3)
print("Коэффициент корреляции между списками =", r)

f.close()
