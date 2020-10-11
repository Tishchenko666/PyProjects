s1 = input("Ключевое слово:")
f = open("input.txt", "r")
f1 = open("output.txt", "w")
c = 0
for s in f:
  if s1 in s:
    c += 1
    s2 = s1.upper()
    s = s.replace(s1, s2)
  f1.write(s)

if c == 0:
  f1.write("The key word is absent in the text.")
f.close()
f1.close()
