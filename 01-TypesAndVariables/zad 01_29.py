import random
użytkownik = int(input('Podaj, ile oczek kostki wyrzucił komputer: '))
komputer = int(random.randrange(1, 7))
print(f'Komputer wyrzucił: {komputer}')
if użytkownik == komputer:
    print('Zgadłeś: True')
else:
    print('Zgadłeś: False')
