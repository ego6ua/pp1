lst = []
f = open('C:/Users/asus/Desktop/pp1/03-FileHandling/numbers.txt','r') 
#print(f.read())
lst.append(list(f))
#print(lst)
for i in lst:
    print(i)
f.close()