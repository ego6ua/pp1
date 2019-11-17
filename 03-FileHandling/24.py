t = [['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]
r = ['Imie', 'Nazwisko', 'Email']
with open('Tablica_imiona.csv', 'w') as f:
    for x in r:    
        f.write(f'{str(x)} ')
    f.write('\n')
    for a in t[0]:
        f.write(f'{str(a)} ')
    f.write('\n')
    for b in t[1]:
        f.write(f'{str(b)} ')
    f.write('\n')
    for c in t[2]:
        f.write(f'{str(c)} ')
    f.write('\n')
    
    '''for i in t:
        for c in i:
            f.write(f'{str(c)} ')
       '''
f.close