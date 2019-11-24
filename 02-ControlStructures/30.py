ppin = '0805'
pin = str(input('Podaj kod PIN: '))
i = 0

while i<3:
    if pin == ppin:
        print('Kod PIN poprawny.')
        break
    else:         
        print('Kod PIN niepoprawny.')
        
        
    i+=1   
    
else:
    print('Karta płatnicza zostaje zablokowana.')