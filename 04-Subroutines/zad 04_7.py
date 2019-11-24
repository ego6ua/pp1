'''def numbers():
    num = (''1 2 3
4 5 6
7 8 9'')
    return num
print(numbers())'''

import re
str = "The rain in Spain"
x = re.findall("Spain", str)
print(x)
if (x):
    print("Yes, there is a match!")
else:
    print("No match")

