#Из предложенного текстового файла (text18-6.txt) вывести на экран его содержимое,
#количество пробельных символов. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно заменив все знаки пунктуации на знак «!».


text = '''Два дня мы были в перестрелке.
Что толку в этакой безделке?
Мы ждали третий день.
Повсюду стали слышны речи:
«Пора добраться до картечи!»
И вот на поле грозной сечи
Ночная пала тень.'''

# Запись текста в текствовый файл для работы
textfile = open(file='text18-6.txt', mode='w', encoding='utf-8')
textfile.writelines(text)
textfile.close()

# Открытие текствого файла для работы с ним
textfile_open = open(file='text18-6.txt', mode='r', encoding='utf-8')
textf_read = textfile_open.read()
# Подсчет пробельных символов в тексте
n = 0
for i in textf_read:
    if i == ' ':
        n += 1
textfile_open.close()
print(textf_read, f'\n\nКоличество пробельных символов в тексте: {n}')

# Символы из текста
symbol = '.«»?:'

# Замена символов из текста
for i in symbol:
    textf_read = textf_read.replace(i, '!')

# Запись нового текста
new_text = open(file='text18-new.txt', mode='w', encoding='utf-8')
new_text.writelines(textf_read)
new_text.close()