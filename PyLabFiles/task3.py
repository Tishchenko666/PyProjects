f = open("x19.txt", "r")
f1 = open("task.csv", "w")
for line in f:
  if not line.startswith("#"):
    l = line.split(" ")
    if len(l) > 2:
      line = line.lstrip().replace(".", ",")
      line_without_space = ""
      previous_symbol = ""
      for i in line:
        if i.isdigit() or i == ",":
          line_without_space += i
        if previous_symbol.isdigit() and i == " ":
          line_without_space += ";"
        previous_symbol = i
      f1.write(line_without_space + "\n")
f.close()
f1.close()
