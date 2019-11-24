print('Imiona: Janek Ania Wojtek Zosia')
im = str(input('Imie: '))
def jestImie(imie):
    imiona = ['Janek', 'Ania', 'Wojtek', 'Zosia']
    if imie in imiona:
        print('Rezultat: imię zawarte jest w wykazie imion')
    else:
        print('Rezultat: imię zawarte nie jest w wykazie imio')
jestImie(im)