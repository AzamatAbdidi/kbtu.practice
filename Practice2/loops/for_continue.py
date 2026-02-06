#1 цикл будет работать до "банан" и затем продолжится 
# в итоге вывод яблоко и вишня
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
