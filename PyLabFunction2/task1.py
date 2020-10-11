def fill_matrice(mf, nf):
  from random import randint
  return [[randint(1, 20) for j in range(nf)] for i in range(mf)]


def info(matrice, mi, ni):
  print("Матрица")
  for i in range(mi):
    for j in range(ni):
      print(str(matrice[i][j]).rjust(3), end=' ')
    print()


def row_median(row, nr):
  from math import ceil, floor
  if nr % 2 != 0:
    return row[floor(len(row) / 2)]
  elif nr % 2 == 0:
    return (row[ceil(len(row) / 2)] + row[floor(len(row) / 2)]) / 2


m = int(input("Число строк: "))
n = int(input("Число столбцов: "))
matrix = fill_matrice(m, n)
info(matrix, m, n)
modes = [row_median(r, n) for r in matrix]
print("Наименьшую медиану имеет строка номер ", modes.index(min(modes)) + 1)
