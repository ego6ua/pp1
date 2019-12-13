print('Rachunek nr: 12 3456 5555 9090 1111 0000 7722')
class Rachunek_Bankowy():
    def __init__(self):
        self.saldo = 0
    
    def wpłać(self, wpłać):
        self.wpłać = wpłać
        self.saldo += float(wpłać)
        
    def wypłać(self, wypłać):
        self.wypłać = wypłać
        if self.saldo >= wypłać:
            self.saldo -= float(wypłać)
        else:
            print('Niewystarczająca ilość środków na rachunku')
    
    def status(self):
        print(f'Saldo: {self.saldo} zł')


rachunek = Rachunek_Bankowy()
rachunek.wpłać(994.30)
rachunek.wypłać(60.70)
rachunek.status()