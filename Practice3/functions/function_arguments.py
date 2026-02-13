def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#1 a function using an argument

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument
#2 a difference between parametr and argument


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
#3 This function expects 2 arguments, and gets 2 arguments


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
#4 This function expects 2 arguments, but gets only 1

def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#5 Default value for country parameter

