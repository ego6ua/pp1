import math
x = 3.7
y = 4
a = math.sqrt(x)
b = x ** y
c = math.pow(x,1/y)
d = math.pi*y**2
e = math.factorial(y)
f = math.floor(x)
print(f'Pierwiastek kwadratowy z {x} wynosi {a:.2f}')
print(f'X do potęgi {y} wynosi {b:.2f}')
print(f'Pierwiastek {y}-tego stopnia z {x} wynosi {c:.2f}')
print(f'Pole koła o promieniu {y} wynosi {d:.2f}')
print(f'Silnię {y} wynosi {e:.2f}')
print(f'Największą możliwą liczbę całkowitą, mniejszą bądź równą {x} wynosi {f}')