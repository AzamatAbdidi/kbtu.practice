# Пример 1
class Car:
    # Переменная класса (общая для всех машин)
    wheels = 4 

    def __init__(self, brand, model):
        # Переменные экземпляра (у каждой машины свои)
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Camry")
car2 = Car("Tesla", "Model 3")

print(car1.brand, car1.wheels) # Toyota 4
print(car2.brand, car2.wheels) # Tesla 4

# Если изменить переменную класса, она изменится для всех
Car.wheels = 6
print(car1.wheels) # 6



# Пример 2
class Employee:
    # Переменная класса для подсчета количества сотрудников
    number_of_employees = 0

    def __init__(self, name):
        self.name = name
        # При создании каждого нового объекта увеличиваем счетчик класса
        Employee.number_of_employees += 1

emp1 = Employee("Sanzhar")
emp2 = Employee("Arman")

print("Total employees:", Employee.number_of_employees) # Выведет 2