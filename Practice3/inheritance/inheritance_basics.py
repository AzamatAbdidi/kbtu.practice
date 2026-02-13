#1 Родительский класс
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#2 Дочерний класс (наследует всё от Person)
class Student(Person):
  pass 

#3 Использование
x = Student("Sanzhar", "Abdygappar")
x.printname() # Метод взят у родителя

