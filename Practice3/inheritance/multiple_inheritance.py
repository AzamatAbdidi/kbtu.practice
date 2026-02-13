# ПРИМЕР 1: Первый родитель
class Employer:
    def company_info(self):
        print("Working at KBTU")

# ПРИМЕР 2: Второй родитель
class Developer:
    def skill_info(self):
        print("Coding in Python")

# ПРИМЕР 3: Множественное наследование
# Класс Intern забирает методы у обоих родителей сразу
class Intern(Employer, Developer):
    pass

# Использование
sanzhar = Intern()
sanzhar.company_info() # Метод от Employer
sanzhar.skill_info()   # Метод от Developer