"""Поезд прибывает на станцию в h1 часов m1 минут, а отправляется в h2 часов m2 минут.
Пассажир пришел на платформу в x часов y минут. Будет ли поезд стоять на платформе?
Все числа вводятся с клавиатуры. При вводе проверять данные на корректность."""

ar_time = input("Прибытие поезда: ")
h1 = ar_time.split(".")
h1 = [int(i) for i in h1]
while h1[0] < 0 or h1[0] > 23 or h1[1] < 0 or h1[1] > 60:
  ar_time = input("Введите корректное значение. Время: ")
  h1 = ar_time.split(".")
  h1 = [int(i) for i in h1]

dep_time = input("Отбытие поезда: ")
h2 = dep_time.split(".")
h2 = [int(i) for i in h2]
while h2[0] < 0 or h2[0] > 23 or h2[1] < 0 or h2[1] > 60:
  dep_time = input("Введите корректное значение. Время: ")
  h2 = dep_time.split(".")
  h2 = [int(i) for i in h2]

pass_ar = input("Приход пассажира: ")
x = pass_ar.split(".")
x = [int(i) for i in x]
while x[0] < 0 or x[0] > 23 or x[1] < 0 or x[1] > 60:
  pass_ar = input("Введите корректное значение. Время: ")
  x = pass_ar.split(".")
  x = [int(i) for i in x]
# Check time here
ar_time = float(ar_time)
dep_time = float(dep_time)
pass_ar = float(pass_ar)
if ar_time <= pass_ar < dep_time:
  print("Да")
else:
  print("Нет")
