day_list = ["Sunday", "Monday", "Thursday", "Wednesday", "Thursday", "Friday", "Saturday"]
print("1.1")
s = day_list[0:4:2]
print(s[0], s[1], day_list[3], day_list[-1], day_list[-2])

print("1.2\n", day_list[:3], day_list[3:4], day_list[4:])

lot_list = [day_list[:3], day_list[3:4], day_list[4:]]
print("1.3\n", lot_list)

lot_list.insert(0, lot_list.pop(len(lot_list) - 1))
lot_list.insert(len(lot_list), lot_list.pop(1))
print("1.4\n", lot_list)

lot_list.append("DAY")
print("1.5\n", lot_list)

lot_list[0].append("Oooo")
print("1.6\n", lot_list)

del lot_list[1:]
print("1.7\n", lot_list)

fio = "Тищенко София Евгеньевна"
print("2\nСтрока:", fio)
print("2.1\nДлинна строки", len(fio))
print("2.2\n", fio[:fio.find(" ")] + ";" + fio[fio.find(" "):fio.rfind(" ")] + ";" + fio[fio.rfind(" "):])
print("2.3\nСимволов o -", fio.count("о"))
print("2.4\nСимволов е -", fio.count("е"))
s = fio.split(" ")
fio_S = s[0] + "\n" + s[1] + "\t" + s[2]
print("2.5\nНовая строка", fio_S)
print("2.6\nДлинна строки", len(fio_S))
