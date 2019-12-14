liczba = int(input('Podaj liczbe: '))
tab = []
def suma(liczba):
    for i in range(1, liczba):
        tab.append(i)
    return sum(tab)
print(suma(liczba))