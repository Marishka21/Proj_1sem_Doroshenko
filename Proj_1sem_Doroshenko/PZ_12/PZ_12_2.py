# Составить генератор (yield), который переведет символы строки из верхнего
# регистра в нижний.
def a (crs: str):
    for ch in crs:
        yield ch.lower()
b = input("Введите слова с помощью Caps Lock: ")
print(''.join(a(b)))