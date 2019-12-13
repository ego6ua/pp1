print('Książka e-book')
print(15 * '=')
class Ksiazka_elektroniczna():
    def __init__(self, tytul, autor, liczba_stron):
        self.stan_k = False
        self.tytul = tytul
        self.autor = autor
        self.liczba_stron = liczba_stron
        self.nr_bieżącej_strony = 1
    
    def otwarta(self):
        self.stan_k = True
        
    def zamknieta(self):
        self.stan_k = False
        
    def set_strona(self, new_nr_strony):
        self.nr_bieżącej_strony = new_nr_strony
    #def set_strona(self, strona):
        #self.nr_bieżącej_strony += strona
        if self.nr_bieżącej_strony > 350:
            self.nr_bieżącej_strony = 350
        if self.nr_bieżącej_strony <= 0:
            self.nr_bieżącej_strony = 1
            
    def status(self):
        print(self.tytul)
        print(self.autor)
        print(f'{self.liczba_stron} stron')
        print(15 * '=')
        if self.stan_k:
            print(f'Książka jest otwarta na stronie {self.nr_bieżącej_strony}')
        else:
            print('Książka jest zamknięta')
        
    
ksiazka = Ksiazka_elektroniczna('Harry Potter', 'J.K.Rowling', 350)
ksiazka.otwarta()
ksiazka.set_strona(1)
ksiazka.status()