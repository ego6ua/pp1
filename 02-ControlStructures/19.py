ciag = ''
x = 1
while (x<100):
    x += 3
    ciag +=str(x)+","

    if x == 100:
        break
print(f'Ciąg arytmetyczny o różnicy 3:{ciag}')