#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов

import random
# Создание и запись цифрового ряда из пол и отриц чисел в файл
num = [random.randint(-20, 20) for i in range(15)]
file_old = open(file='numbers.txt', mode='w', encoding='utf-8')
file_old.writelines([str(i) + ' ' for i in num])
file_old.close()

# Чтение и использование раннее созданных данных
numbers = open(file='numbers.txt', mode='r', encoding='utf-8')
numbers_list = numbers.read().split()
numbers.close()
print(numbers_list)

# Подсчет произведения массива
prod = 1
for i in numbers_list:
    prod *= int(i)

# Нахождение повторяющихся элементов
temp = []
temp1 = []
for i in numbers_list:
    if i in temp:
        temp1.append(i)
    else:
        temp.append(i)


text_file = open(file='numfile.txt', mode='w', encoding='utf-8')
# Запись в новый файл тех данных, которые требуются в условии
text_file.writelines(f'''Исходные данные: {numbers_list}
Количество элементов: {len(numbers_list)}
Произведение элементов: {prod}
Повторяющиеся элементы: {temp1}
Количество повторяющихся элементов: {len(numbers_list) - len(list(set(numbers_list)))}
Элементы больше 5 увеличены в два раза: {[i*2 for i in map(int, numbers_list) if i > 5]}''')
text_file.close()