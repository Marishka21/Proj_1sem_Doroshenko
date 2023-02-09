#Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0

import random

def matrix():
    x = int(input("Количество строк матрицы: "))
    y = int(input("Количество столбцов в матрице: "))
    return [[random.randint(-100,100) for i in range(y)] for j in range(x)]
b = matrix()
print(b)
c = [[0 if k > 10 else k for k in i] for i in b]
print(c)