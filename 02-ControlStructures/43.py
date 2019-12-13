a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))
c = int(input('Podaj trzecią liczbę: '))
if a<=b and a<=c:
    min = a
    if b<=c:
        max = c
        sr = b
    else:
        max = b
        sr = c
if b<=a and b<=c:
    min = b
    if a<=c:
        max = c
        sr = a
    else:
        max = a
        sr = c
if c<=a and c<=b:
    min = c
    if a<=b:
        max = b
        sr = a
    else:
        max = a
        sr = b
print(f'Liczby w kolejności rosnącej: {min, sr, max}')