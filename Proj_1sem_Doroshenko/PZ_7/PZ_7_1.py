#Дан символ С, изображающий цифру или букву (латинскую или русскую).
#Если С изображает цифру, то вывести строку "digits", если латинскую
#букву - вывести строку "lat", если русскую - вывести строку "rus".

import random
ru = u"абвгдеёзийклмнопрстуфхъыьэАБВГДЕЁЗИЙКЛМНОПРСТУФХЪЫЬЭ"
en = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = u"0123456789"
letters = ru + en + digits
C = random.choice(letters)
print("Символ: ",C)
if ru.find(C) != -1:
    print("rus")
elif en.find(C) != -1:
    print("lat")
elif digits.find(C) != -1:
    print("digit")