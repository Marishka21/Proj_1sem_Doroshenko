# Создайте класс «Книга», который имеет атрибуты название, автор и количество
# страниц. Добавьте методы для чтения и записи книги
class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

    def read(self):
        print(f"Reading {self.title} by {self.author}...")

    def write(self):
        print(f"Writing {self.title} by {self.author}...")

# Пример использования класса "Книга"
my_book = Book("Pride and Prejudice", "Jane Austen", 416)
my_book.read()  
my_book.write()  