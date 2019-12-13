import re
komunikat = 'wtorek - 23C, środa - 21C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
a = int(cyfry[0])
b = int(cyfry[1])
c = int(cyfry[2])
x = a, b, c
y = sum(x)/len(cyfry)
print(f'srednia temperatura to: {int(y)}C')

with open('Temperatura.txt', 'w')as f:
    f.write(f'srednia temperatura to: {int(y)}C')
f.close
