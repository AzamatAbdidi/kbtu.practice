#1 The findall() function returns a list containing all matches.
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#2 The search() function searches the string for a match, and returns a Match object if there is a match.
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

#3 The split() function returns a list where the string has been split at each match:
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#4 The sub() function replaces the matches with the text of your choice:
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# A Match Object is an object containing information about the search and the result.
#5 Do a search that will return a Match Object:
import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

#6 The regular expression looks for any words that starts with an upper case "S":

import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

#7 Print the string passed into the function:

import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

#8 The regular expression looks for any words that starts with an upper case "S":
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

