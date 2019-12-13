#pin = str(input('Podaj kod PIN: '))
praw_pin = '0805'
i=0
while i <= 3:
    pin = str(input('Podaj kod PIN: '))
    if pin == praw_pin:
        print('Kod PIN poprawny.')
        break
    else:
        print('Kod PIN niepoprawny.')
        i+=1
        if i == 3:
            print('Karta zostanie zablokowana')
            break
