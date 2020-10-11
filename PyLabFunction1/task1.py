def len_point_start(point):
  from math import sqrt
  return round(sqrt(point[0] ** 2 + point[1] ** 2), 2)


def trans_inp(p1):
  return [int(k) for k in p1.split(" ")]


p = input("Координаты точки: ")
print("Расстоянеи от точки до начала координат = ", len_point_start(trans_inp(p)))
