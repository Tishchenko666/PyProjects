"""Конфеты. Известна цена 1 кг конфет «Spam!». Вывести на экран таблицу стоимостей
100, 200, 300, ..., 1000 г этих конфет.
"""

x = int(input("Цена: "))
for i in range(1, 11):
  p = x * i / 10
  print(i * 100, "\t", p)
