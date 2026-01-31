#1 пример с Тру фолс стейтмент. 
print(10 > 9) #тру 
print(10 == 9)  #фолс
print(10 < 9)  #фолс

#2 тот же тру фолс, но вместе с условиями
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#3 Оценка значений через bool()
print(bool("Hello")) # то есть здесь результат должен быть Тру 
print(bool(15)) # here is the same but eith number

#4 Значения, которые возвращают False
print(bool(False))
print(bool(None))
print(bool(0))

#5 Print "YES!" if the function returns True, otherwise print "NO!": 
"""
функция с использованием булл. Здесь мы как бы внутрий функций используем ретерн и говорим
верни мою функцию как Тру. Дальше условия проверяются и результатом будет Тру
"""
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")