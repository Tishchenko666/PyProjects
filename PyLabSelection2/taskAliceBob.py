alice_date = input("Дата рождения Алисы через точку: ")
bob_date = input("Дата рождения Боба через точку: ")
al = alice_date.split(".")
bl = bob_date.split(".")
ad = [int(i) for i in al]
bd = [int(j) for j in bl]
if min(ad[2], bd[2]) in ad:
  print("Алиса старше")
elif ad[2] == bd[2]:
  if min(ad[1], bd[1]) in ad:
    print("Алиса старше")
  elif ad[1] == bd[1]:
    if min(ad[0], bd[0]) in ad:
      print("Алиса старше")
    elif ad[0] == bd[0]:
      print("Их возраст совпадает")
    else:
      print("Боб старше")
  else:
    print("Боб старше")
else:
  print("Боб старше")
