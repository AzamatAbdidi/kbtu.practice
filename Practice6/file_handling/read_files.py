'''
To open the file, use the built-in open() function.
The open() function returns a file object, 
which has a read() method for reading the content of the file:
'''
#1 
f = open("demofile.txt")
print(f.read())

#2 If the file is located in a different location, you will have to specify the file path, like this:
f = open("D:\\myfiles\welcome.txt")
print(f.read())


#3 Using the with keyword:
#Then you do not have to worry about closing your files, the with statement takes care of that.

with open("demofile.txt") as f:
  print(f.read())

#4 Close the file when you are finished with it:

f = open("demofile.txt")
print(f.readline())
f.close()

#5 By default the read() method returns the whole text, 
# but you can also specify how many characters you want to return:
# Return the 5 first characters of the file:
with open("demofile.txt") as f:
  print(f.read(5))

#6 You can return one line by using the readline() method:
with open("demofile.txt") as f:
  print(f.readline())

#7 By calling readline() two times, you can read the two first lines:
with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())


#8 By looping through the lines of the file, you can read the whole file, line by line:
with open("demofile.txt") as f:
  for x in f:
    print(x)
    