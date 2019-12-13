class Ulamek_zwykly():
    def __init__(self, licznik, mianownik):
        self.licznir = licznik
        self.mianownik = mianownik

    def print_ulamek(self):
        print(f'{self.licznir}/{self.mianownik}')
        ulamek = self.licznir/self.mianownik
        print(ulamek)

ulamek = Ulamek_zwykly(12, 21)
ulamek.print_ulamek()