f = open("_task5.txt", "r")
letters = set()
for line in f:
  for s in line:
    if line.count(s) >= 2:
      letters.add(s)
print(letters)
