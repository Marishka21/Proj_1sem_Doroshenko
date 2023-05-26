# Создание базового класса "Фигура" и его наследование для создания классов
# "Квадрат", "Прямоугольник" и "Круг". Класс "Фигура" будет иметь общие методы,
# такие как вычисление площади и периметра, а классы-наследники будут иметь
# специфичные методы и свойства. 

class Figura:
     def __init__(self, a, b):
        self.a = a
        self.b = b

    
class Square(Figura):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.a = a
        self.b = b

    def s(self):
        return self.a*self.b
        
    def pr(self):
        return (self.a+self.b)*2    

class Rectangle(Figura):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.a = a
        self.b = b

    def s(self):
        return self.a*self.b
        
    def pr(self):
        return (self.a+self.b)*2 
class Circle(Figura):   
    def __init__(self, a, b):
        super().__init__(a, b)
        self.a = a
        self.b = b

    def s(self):
        return self.a*self.a*3.14

 # Пример 
c = Circle(9, 18)
print(c.s())
s = Square(3, 3)
print(s.pr())
print(s.s())
r = Rectangle(5, 4)
print(r.pr())
print(r.s())
      