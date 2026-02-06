#1 остановит цикл на нужном результате "яблоко, банан"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#2 здесь цикл остановится до принта поэтому результат будет"яблоко"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)