import re
f = open('C:/Users/asus/Desktop/pp1/03-FileHandling/land.txt', 'r')
cyfry = []
for i in f:
    cyfry += re.findall(r'\d', i)
suma = 0
for l in cyfry:
    suma+=int(l)
print(f"SUMA: {suma}")    
f.close()