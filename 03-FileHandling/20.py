import re
f = open('C:/Users/asus/Desktop/pp1/03-FileHandling/numbers.txt','r') 
w = open('C:/Users/asus/Desktop/pp1/03-FileHandling/evennumbers.txt', 'a')
file = f.read()
liczby = re.findall(r'\d{3}', file)
for i in liczby:
    if int(i)%2==0:
        w.write(f'{i}\n')
f.close()
w.close()