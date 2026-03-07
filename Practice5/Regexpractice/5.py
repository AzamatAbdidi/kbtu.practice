import re
s = input()
if re.search(r"a.*b$", s):
    print("Match")
else:
    print("No match")