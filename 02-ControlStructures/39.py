ciag = [0,1]
for i in ciag:
    print(i, end=' ')
for n in range(30):
    l = ciag[-1]+ciag[-2]
    ciag.append(l)
    print(l, end=' ')
