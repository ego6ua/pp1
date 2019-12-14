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



print(55*'=')
import re
tekst = ('Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.')
print(tekst)
a = re.findall('a|A', tekst)
la = len(a)
i = re.findall('i|I', tekst)
li = len(i)
e = re.findall('e|E', tekst)
le = len(e)
y = re.findall('y|Y', tekst)
ly = len(y)
u = re.findall('u|U', tekst)
lu = len(u)
o = re.findall('o|O', tekst)
lo = len(o)
an = re.findall("Ą|ą",tekst)
lan = len(an)
en = re.findall("Ę|ę",tekst)
lenn = len(en)

print(f'a: {la} e: {le} i: {li} y: {ly} u: {lu} o: {lo} ą: {lan} ę: {lenn}')


