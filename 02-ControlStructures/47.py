kwota = int(input('Podaj kwotę w zł: '))
moneta1 = 0
moneta2 = 0
moneta5 = 0
if kwota%5 == 0:
    moneta5 += kwota//5
elif kwota%5 != 0: #and kwota%2 == 0:
    reszta5 = kwota%5
    reszta2 = reszta5%2
    moneta5 += kwota//5
    moneta2 += reszta5//2
    moneta1 += reszta2
print(f'Kwota {kwota} zł w monetach:\n5 zł – {moneta5} szt\n2 zł – {moneta2} szt\n1 zł – {moneta1} szt')


#albo:
'''kwota=int(input("Podaj kwotę w zł: "))
monety=[5,2,1]
i=0
while (kwota>0):
    if (kwota>=monety[i]): 
        p=int(kwota/monety[i]) #ile razy wydac dany nominal
        kwota=kwota-(monety[i]*p) #zmniejszanie kwoty o wydany nominal
        print(f"{monety[i]} zl - {p} szt") #wypisz wynik 
    i+=1  #kolejny nominal
    '''