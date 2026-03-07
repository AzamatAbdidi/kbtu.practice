import re
s = input()
words = s.split('_')
res = words[0] + ''.join(x.title() for x in words[1:])
print(res)