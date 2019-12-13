a = input('Podaj liczbe a: ')
b = input('Podaj liczbe b: ')
c = input('Podaj liczbe c: ')
import math
a = int(a)
b = int(b)
c = int(c)
d = b**2 - 4*a*c
D = math.sqrt(d)
x1 = (-b+D)/2*a
x2 = (-b-D)/2*a
print(a, 'x^2', '+', b, 'x', '+', c, '=', '0', end='')
print(f'D = {D}')
print(f'X1 = {x1}')
print(f'X2 = {x2}')
