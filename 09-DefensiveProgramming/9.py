import math
while (1 == 1):
    try:
        number = float(input('Enter any number: '))
        print (f'sqrt({number}) = {math.sqrt(number)}' )
        break
    except:
        print('Please enter a valid number greater than 0')