imiona = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy', 'Teofil']
maks = 0
for i in imiona:
    dlug = len(i)
    if dlug>maks:
        maks = dlug
        imie = i
print(imie)