#1 \A	Returns a match if the specified characters are at the beginning of the string
import re
txt = "The rain in Spain"
#Check if the string starts with "The":
x = re.findall("\AThe", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")

#2 \b	Returns a match where the specified characters are at the beginning or at the end of a word
import re
txt = "The rain in Spain"
# Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#3  (the "r" in the beginning is making sure that the string is being treated as a "raw string")
import re
txt = "The rain in Spain"
#Check if "ain" is present at the end of a WORD:
x = re.findall(r"ain\b", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
