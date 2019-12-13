tablica = []
with open('C:/Users/asus/Desktop/pp1/03-FileHandling/universities.txt', 'r') as file:
    for i in file:
        tablica.append(str(i))
file.close()
tablica.sort()
f=open("C:/Users/asus/Desktop/pp1/03-FileHandling/universities.txt").readlines()
c=open("C:/Users/asus/Desktop/pp1/03-FileHandling/universities.txt","w")
j=0
for l in f:
    c.write(str(l).replace(str(l),tablica[j]))
    j+=1
c.close()
