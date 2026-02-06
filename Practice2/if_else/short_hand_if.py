#1 шорт хэнд иф дает возможность писать инструкцию сразу на одной строке
a = 5
b = 2
if a > b: print("a is greater than b")
#2 использование иф и елсе в одной строке
a = 2
b = 330
print("A") if a > b else print("B")
#3 можно прямо вместе с иф объявить новый ввариебл
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#4 максимум среди двух значении
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)
