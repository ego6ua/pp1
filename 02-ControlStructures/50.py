liczba = int(input('Podaj liczbe dziesiętna: '))
binarna = ''
binarna_od = ''
while liczba != 0:
    if liczba%2 == 0:
        binarna += '0'
    else:
        binarna += '1'
    liczba = int(liczba/2)
l = len(binarna)-1
for i in range(l, -1, -1):
    binarna_od += binarna[i]
print(f'Liczba binarna: {binarna_od}')
    


