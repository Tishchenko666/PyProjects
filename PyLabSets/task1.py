num = 1
while True:
  sqrt_num = str(num ** 2)
  if len(sqrt_num) == 10:
    if len(set(sqrt_num)) == 10:
      print("Квадрат числа", num, "дает 10-значное число с различными цифрами", sqrt_num)
      break
    else:
      num += 1
  else:
    num += 1
