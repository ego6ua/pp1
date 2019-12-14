def liczby(li, x, y):
    if li>=x and li<=y:
        return True
    else:
        return False
li = int(input('Podaj liczbe: '))
x = int(input('Zakres 1: '))
y = int(input('Zakres 2: '))
print(liczby(li, x, y))