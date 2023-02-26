# Из исходного текстового файла (ip_address.txt) из раздела «Зарезервированные
# адреса» перенести в первый файл строки с ненулевыми первым и вторым октетами,
# а во второй – все остальные. Посчитать количество полученных строк в каждом
# файле.

import re

with open("ip_adress.txt", encoding="UTF-8") as f:
    f2 = f.readlines()
    str_li = ""
    str_li_2 = ""
    count_1, count_2 = 0, 0
    for k in f2:
        if re.findall(r"Зарезервированные адреса", k):
            index_line = re.search(r"Зарезервированные адреса", k)
            for i in f2[index_line.span()[1]::]:
                if re.search(r"^\d{1,3}.[1-9]\d{1,2}.\d{1,3}.\d{1,3}", i):
                    str_li += i
                    count_1 += 1
                else:
                    count_2 += 1
                    str_li_2 += i

#Запись во второй файл данных.
with open("first.txt", "w", encoding="UTF-8") as f2:
    f3 = f2.write(str_li) #Запись данных в файл.
    f3 = f2.write(f"\nПолученных строк {count_1}")

#Запись в третий файл данных.
with open("second.txt", "w", encoding="UTF-8") as f4:
    f5 = f4.write(str_li_2) #Запись данных в файл.
    f5 = f4.write("\nПолученных строк %s" % str(count_2))