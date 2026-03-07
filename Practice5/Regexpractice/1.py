import re
s = input()
if re.search(r"ab*", s):
    print("Match")
else:
    print("No match")