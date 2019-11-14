import re
komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
a = int(cyfry[0])
b = int(cyfry[1])
c = int(cyfry[2])
x = a, b, c
y = sum(x)/len(cyfry)
print(f'srednia temperatura to: {y:.2f}')

with open('Temperatura.txt', 'w')as f:
    f.write(f'srednia temperatura to: {y:.2f}')
f.close
