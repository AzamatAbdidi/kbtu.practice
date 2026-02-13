# ПРИМЕР 1: Родительский класс
class Person:
    # ПРИМЕР 2: Конструктор (self — ссылка на объект)
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

# ПРИМЕР 3: Наследование
class Student(Person):
    def __init__(self, fname, lname, year):
        # ПРИМЕР 4: super() вызывает родительский конструктор
        super().__init__(fname, lname)
        self.graduationyear = year

# ПРИМЕР 5: Создание объекта
x = Student("Arman", "Ivanov", 2024)
print(x.graduationyear)