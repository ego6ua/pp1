import re
f = open('C:/Users/asus/Desktop/pp1/03-FileHandling/numbers.txt','r') 
file = f.read()
liczby = re.findall(r'\d{3}', file)
for i in liczby:
    print(i, end=' ')