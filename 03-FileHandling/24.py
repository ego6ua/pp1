t = [['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]
r = ['Imie', 'Nazwisko', 'Email']
with open('Tablica_imiona.csv', 'w') as f:
    f.write(f'{str(r)}\n')
    for i in t:
        f.write(f'{str(i)}\n') 
f.close