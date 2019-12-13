suma = 0
liczby = 0
i = 1
while i != 0:
    i = int(input('Podaj liczbe: '))
    #liczby += 1
    if i != 0:
        suma += i
        liczby += 1
srednia = suma/liczby
print(f'RESULT: Liczb: {liczby}, Suma = {suma}, Srednia = {srednia}')