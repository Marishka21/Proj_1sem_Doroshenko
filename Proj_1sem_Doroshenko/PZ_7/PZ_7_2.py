#Дана строка-предложение на русском языке. Зашифровать ее, выполнив
#циклическую замену каждой буквы на следующую за ней в алфавите и сохранив при
#этом регистр букв («А» перейдет в «Б», «а» — в «б», «Б» — в «В», «я» — в «а» и т.
#д.). Букву «ё» в алфавите не учитывать («е» должна переходить в «ж»). Знаки
#препинания и пробелы не изменять.
a = 'Мою собаку зовут Роки'
print(a)
lis = u"абвгдежзийклмнопрстуфхчцъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЧЦЪЫЬЭЮЯ"
for i in range(len(a)):
    if a[i] in lis:
        try:
            print(lis[lis.index(a[i])+1],end='')
        except IndexError:
            print(lis[0])