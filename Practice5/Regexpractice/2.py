import re
s = input()
if re.search(r"ab{2,3}", s):
    print("Match")
else:
    print("No match")
