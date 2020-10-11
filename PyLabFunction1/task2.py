from task1 import len_point_start, trans_inp

a = input("A = ")
b = input("B = ")
c = input("C = ")
dists = [len_point_start(trans_inp(a)), len_point_start(trans_inp(b)), len_point_start(trans_inp(c))]
min_p = min(dists)
max_p = max(dists)
k = 0
for i in dists:
  if i == min_p:
    if k == 0:
      print("Наиболее близка к началу координат точка A")
    elif k == 1:
      print("Наиболее близка к началу координат точка B")
    else:
      print("Наиболее близка к началу координат точка C")
  if i == max_p:
    if k == 0:
      print("Наиболее далека от начала координат точка A")
    elif k == 1:
      print("Наиболее далека от начала координат точка B")
    else:
      print("Наиболее далека от начала координат точка C")
  k += 1
