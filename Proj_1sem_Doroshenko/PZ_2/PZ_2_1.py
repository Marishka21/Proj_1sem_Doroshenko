try:
    L = int(input('Введите расстояние в сантиметрах: ')) #Дано расстояние L в сантиметрах
    M = L//100 #Операция деления нацело
    print(M) #Результат
except:
    print('Введите число!')
