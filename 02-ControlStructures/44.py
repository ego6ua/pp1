limit = int(input("Podaj limit prędkości(km/h): "))
predkosc=int(input("Podaj prędkość pojazdu(km/h): "))
r = predkosc-limit
if r>10:
    mandat = (r-10)*15 + 50
else:
    mandat = r*5
print(f'Mandat (zł): {mandat}')
    