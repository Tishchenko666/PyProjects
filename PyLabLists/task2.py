from random import randint

students_list = []
size = int(input("Длинна саписка = "))
action = int(input("Ввод:\n1 - с клавиатуры\n2 - из файла\n3 - заполнение случайными числами\n>>"))
if action == 1:
  for i in range(size):
    students_list.append(int(input("Рост ученика: ")))
  print("Список ростов =", students_list)
elif action == 2:
  file_name = input("Файл: ")  # use hightes.txt for test it
  f = open(file_name, "r")
  line = f.read()
  f.close()
  students_list = line.split(";")
  for j in range(len(students_list)):
    students_list[j] = int(students_list[j])
  print("Список ростов =", students_list)
elif action == 3:
  students_list = [randint(160, 191) for n in range(size)]
  print("Список ростов =", students_list)
average_height = round(sum(students_list) / len(students_list), 2)
counter = 0
for h in students_list:
  if h < average_height:
    counter += 1
print(counter, "учеников имеют рост ниже среднего")
