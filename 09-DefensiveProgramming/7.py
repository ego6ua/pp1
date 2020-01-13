wzrost = int(input('Podaj swoj wzrost w cm: '))
waga = float(input('Podaj swoje wage w kg: '))
assert type(wzrost) == int, 'Type wzrost nie jest int!'
assert type(waga) == float, 'Type waga nie jest float!'
assert wzrost >= 150 and wzrost <= 220, 'Wzrost nie jest w przedziale!'
assert waga >= 40.0 and waga <= 150.0, 'Waga nie jest w przedziale!'
print(f'BMI: {waga/(wzrost*wzrost/10000)}')