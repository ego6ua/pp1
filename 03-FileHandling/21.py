tab = []
with open ('C:/Users/asus/Desktop/pp1/03-FileHandling/numbersinrows.txt', 'r') as f:
    for i in f:
        x = i.split(',')
        tab += x
f.close()
l=len(tab)
suma=0
for i in tab:
    suma+=int(i)
print(f"W pliku znajduje się {l} liczb, a ich suma wynosi {suma}") 