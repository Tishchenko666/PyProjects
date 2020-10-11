# Какое равенство точнее

equality1 = "83^1/2 = 9.11"
equality2 = "6/11 = 0.545"

a1 = 83 ** (1 / 2)
a2 = 6 / 11
a1_round = round(a1, 2)
a2_round = round(a2, 3)
alfa_a1 = abs(a1 - a1_round)
alfa_a2 = abs(a2 - a2_round)
delta_a1 = round(alfa_a1 / a1_round, 6) * 100
delta_a2 = round(alfa_a2 / a2_round, 5) * 100
if delta_a1 < delta_a2:
  print(equality1, "is more accurate")
elif delta_a1 > delta_a2:
  print(equality2, "is more accurate")
else:
  print(equality1, "and", equality2, "have the same accuracy")
