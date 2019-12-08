print('Książka e-book')
print(15 * '=')
class Ksiazka_elektroniczna():
    def __init__(self):
        self.stan_k = False
        
    def otwarta(self):
        self.stan_k = True
        
    def zamknieta(self):
        self.stan_k = False
        
    def status(self):
        if self.stan_k:
            print('Książka jest otwarta')
        else:
            print('Książka jest zamknięta')
        
    
ksiazka = Ksiazka_elektroniczna()
ksiazka.otwarta()
ksiazka.status()