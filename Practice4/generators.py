#1 A simple generator function:
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

#2 Generator that yields numbers:
# When yield is encountered, the function's state is saved, and the value is returned. 
# The next time the generator is called, it continues from where it left off.

def count_up_to(n):
 count = 1
 while count <= n:
    yield count
 count += 1

for num in count_up_to(5):
  print(num)

#3 Generator for large sequences:

def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))


#4 You can manually iterate through a generator using the next() function
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

#5 result [0, 1, 4, 9, 16]
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))