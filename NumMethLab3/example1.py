def error_multiply(x, y, d_x, d_y):
  return abs(x) * d_y + abs(y) * d_x + d_x * d_y


def error_division(x, y, d_x, d_y):
  return (abs(x) * d_y + abs(y) * d_x) / (y ** 2)


a = 0.643
b = 2.17
c = 5.843
delta_a = delta_b = delta_c = 0.01
b2 = error_multiply(b, b, delta_b, delta_b)
b3 = error_multiply(b ** 2, b, b2, delta_b)
ab3 = error_multiply(a, b ** 3, delta_a, b3)
delta_z = error_division(a * b ** 3, c, ab3, delta_c)
f = a * b ** 3 / c
z1 = str(f) + "+-" + str(delta_z)
z2 = round(f, 1)
print("f = ab^3/c")
print("Error =", delta_z)
print("f =", z1, "=", z2)
