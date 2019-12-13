f = open('C:/Users/asus/Desktop/pp1/03-FileHandling/students.txt', 'r')
p = (f.read())
for i in p:
    if i == ',':
        print('', end = '  ')
    else:
        print(i, end = '')
    print(i)
        
