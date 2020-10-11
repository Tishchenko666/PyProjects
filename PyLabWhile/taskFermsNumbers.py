from math import sqrt

ch_num = 4
p = 0
while p == 0:
  num = ch_num + 1
  if num < 70000:
    all_nums = set(range(2, num))
    not_prime = set()
    for x in all_nums:
      if x not in not_prime:
        i = 2
        while x * i in all_nums:
          not_prime.add(x * i)
          i += i
    prime_nums = all_nums - not_prime
    for k in prime_nums:
      if num % k == 0:
        print("Значение", num, "на простые множители", k, "и", num // k)
        print("Это значение опровергает теорию Ферма")
        p = num
        break
    else:
      ch_num = ch_num ** 2
  else:
    start_num = 2
    temp_num = int(sqrt(ch_num)) + 1
    check = True
    while check:
      all_nums = set(range(start_num, temp_num))
      not_prime = set()
      for x in all_nums:
        if x not in not_prime:
          i = 2
          while x * i in all_nums:
            not_prime.add(x * i)
            i += i
      prime_nums = all_nums - not_prime
      for k in prime_nums:
        if num % k == 0:
          print("Значение", num, "на простые множители", k, "и", num // k)
          print("Это значение опровергает теорию Ферма")
          p = num
          check = False
          break
      else:
        start_num = temp_num
        temp_num += temp_num
