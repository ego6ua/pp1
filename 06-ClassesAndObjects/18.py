from random import randrange
class Gra():
    def __init__(self):
        self.rzut1 = 0
        self.rzut2 = 0
        self.rzut3 = 0
    
    def rzucam(self):
        rzucam1 = randrange(1, 6)
        rzucam2 = randrange(1, 6)
        rzucam3 = randrange(1, 6)
        self.rzut1 += rzucam1
        self.rzut2 += rzucam2
        self.rzut3 += rzucam3

    def result(self):
        print(f'RESULT: {self.rzut1} {self.rzut2} {self.rzut3}')
        suma = self.rzut1 + self.rzut2 + self.rzut3
        print(f'SUMA: {suma}')
        
        
gra = Gra()
gra.rzucam()
gra.result()

