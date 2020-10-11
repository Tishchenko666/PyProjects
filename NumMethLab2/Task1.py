from math import sqrt, sin, cos


def tester1(x):
  if 7 + x == 0:
    return False
  elif 5 + 6 / (7 + x) == 0:
    return False
  elif 3 + 4 / (5 + 6 / (7 + x)) == 0:
    return False
  else:
    return True


def tester3(a, b):
  if b == 0:
    return False
  elif a + b == 0:
    return False
  elif a - b == 0:
    return False
  else:
    return True


def fraction1(x, coef=2):
  if tester1(x):
    if coef == 8:
      return (coef - 1) + x
    else:
      return (coef - 1) + coef / fraction1(x, coef + 2)
  else:
    return "This value x is not valid"


def task1():
  x1 = int(input("Task 1.1\nNumber = "))
  result = fraction1(x1)
  if isinstance(result, str):
    print(result)
  else:
    print("Result =", round(result, 3))


def task2():
  x2 = pow(2.468 / ((3.69 / sqrt(10 ** 3)) ** (1 / 3)), 1 / 5)
  y2 = 25 / (125 / pow(6.99 / 300000 ** 2, 1 / 9))
  return (x2 ** 2 + y2 ** 2) / (1 - (x2 ** 2 - y2 ** 2) / 2)


def task3():
  x3 = int(input("Task 1.3\nNumber = "))
  if x3 - 5 > 0:
    a = sqrt(2 * x3)
    b = sqrt(x3 - 5)
    if tester3(a, b):
      res = (a / b) / ((a - b) / (a + b) - (a + b) / (a - b))
      print("Result = ", res)
    else:
      print("This value x is not valid")
  else:
    print("This value x is not valid")


def task4():
  print("Task 1.4\nResult = ", 1 / (sqrt(1 + sin(1 / sqrt(2 + cos(1 / sqrt(3 + sin(1 / 4))))))))


task1()
print("Task 1.2\nz =", task2())
task3()
task4()
