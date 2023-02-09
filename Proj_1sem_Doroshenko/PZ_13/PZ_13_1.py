#в матрице элементы первого столбца возвести в куб

from random import *

a = int(input("Количество строк матрицы: "))
b = int(input("Количество столбцов в матрице: "))
n = 1
print("Матрица: ")
matr = [[randint(-10,10) for j in range(a)] for i in range(b)]
for d in matr:
    print(d)
print('\n', "Новая матрица: ")
for i in matr:
    i[n-1] = i[n-1]**3
    print(i)