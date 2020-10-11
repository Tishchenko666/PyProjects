sides = input("Стороны треугольника через пробел:")
s = sides.split(" ")
a = float(s[0])
b = float(s[1])
c = float(s[2])
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
  if c ** 2 == a ** 2 + b ** 2:
    print("Этот триугольник прямоугольный")
  else:
    print("Этот триугольник не прямоугольный")
else:
  print("Такого треугольника не существует")
