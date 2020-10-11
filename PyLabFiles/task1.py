from random import randint

f = open("numbers.txt", "w")
for i in range(20):
  x = randint(100, 1000)
  f.write(str(x) + "\n")
f.close()
f1 = open("numbers.txt", "r")
f2 = open("final.txt", "w+")
s = f1.read().split("\n")
s.remove("")
t = 0
num_sum = 0
for i in s:
  num = int(i)
  a = num // 100
  b = (num // 10) % 10
  c = num % 10
  if (a * b * c) % (a + b + c) == 0:
    f2.write(str(num) + "\n")
    num_sum += num
    t += 1
if t == 0:
  f2.write(str(t))
  f2.write("Sum of number in this file = 0")
else:
  f2.write("Sum of number in this file = " + str(num_sum))
f1.close()
f2.close()
