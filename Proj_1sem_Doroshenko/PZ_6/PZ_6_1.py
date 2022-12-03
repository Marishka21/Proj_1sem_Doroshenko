#даны целые числа N(>2), A и B. Сформировать и вывести целочисленный список
#размера 10, первый элемент которого равен А, второй равен B, а каждый следущий
#равен сумме всех предыдущих.

import random
import math
N = random.randrange(3,15)
A = random.randrange(-5,5)
B = random.randrange(-5,5)
print("N = ", N)
print("A = ", A)
print("B = ", B)
a = [A,B]
for i in range(2,10):
    x = a[i-2] + a[i-1]
    a.append(x)
print(a)