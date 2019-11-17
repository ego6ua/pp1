f = open('C:/Users/asus/Desktop/pp1/03-FileHandling/land.txt', 'r')
print(f.read())
p = f.read()
import re
cyfry = re.findall('\d',p)
print(cyfry)