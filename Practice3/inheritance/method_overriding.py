# ПРИМЕР 1: Базовый класс (Parent)
class Animal:
    def speak(self):
        print("Animal makes a sound")

# ПРИМЕР 2: Переопределение метода (Method Overriding)
# Дочерний класс Dog заменяет стандартный метод speak своим собственным
class Dog(Animal):
    def speak(self):
        print("Dog barks")

# ПРИМЕР 3: Еще одно переопределение
# Класс Cat тоже меняет поведение родительского метода
class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Использование объектов
my_dog = Dog()
my_dog.speak() # Выведет: Dog barks (вызван переопределенный метод)