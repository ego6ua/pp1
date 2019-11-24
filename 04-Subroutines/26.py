D = int(input('Podaj dochód: '))
def podatek(dochod):
    if D <= 5000:
        pod = (D*17)/100
        print(f'Podatek należny: {int(pod)} zł')
    else:
        pd = (D*32)/100
        print(f'Podatek należny: {int(pd)} zł')
podatek(D)