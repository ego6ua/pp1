pesel = str(input('Podaj Pesel: '))
if int(pesel[9])%2 == 0:
    print('Płeć: kobieta')
else:
    print('Płeć: mężczyzna')

wiek = 2018 - int('19' + pesel[0:2]) 
print(f'Wiek: {wiek}')