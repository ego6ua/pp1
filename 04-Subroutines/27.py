import re
tekst = ('Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.')
print(tekst)
x = re.findall('[aieuoy]', tekst)
from collections import Counter
c = Counter(x)
a = c['a']
i = c['i']
e = c['e']
u = c['u']
y = c['y']
o = c['o']
print(f'a: {a}', f'i: {i}', f'e: {e}', f'u: {u}', f'y: {y}', f'o: {o}')


