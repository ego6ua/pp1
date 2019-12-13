nazwy = ['jeden', 'dwa', 'trzy', 'cztery', 'pec', 'szesc', 'siedem', 'osiem', 'dziewiec', 'dziesiec']
liczba = str(input('Podaj liczbe: '))
print(liczba, '-', end=' ')
for i in liczba:
    i = int(i)
    print(nazwy[i-1], end=' ')
