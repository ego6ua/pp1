from random import randrange
jeden = 0
dwa = 0
trzy = 0
cztery = 0
piec = 0
szesc = 0
for i in range(100):
    li = randrange(1,7)
    if li == 1:
        jeden += 1
    elif li == 2:
        dwa += 1
    elif li == 3:
        trzy += 1
    elif li == 4:
        cztery += 1
    elif li == 5:
        piec += 1
    else:
        szesc += 1
print(f'Jeden: {jeden}\nDwa: {dwa}\nTrzy: {trzy}\nCztery: {cztery}\nPiec: {piec}\nSzesc: {szesc}')