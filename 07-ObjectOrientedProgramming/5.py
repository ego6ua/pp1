class Utwory_muzyczne():
    def __init__(self, wykonawca, tytul, album, rok):
        self.wykonawca = wykonawca
        self.tytul = tytul
        self.album = album
        self.rok = rok
    
    def __str__(self):
        return f'\nWykonawca: {self.wykonawca}\nUtwór:     {self.tytul}\nAlbum:     {self.album}\nRok:       {self.rok}'
    
        
utwory = Utwory_muzyczne('Dawid Podsiadło', 'Nie ma fal', 'Małomiasteczkowy', '2018')
print(utwory)
utwory = Utwory_muzyczne('Dawid Klaus', 'Ja', 'Miasto Krakow', '2016')
print(utwory)
utwory = Utwory_muzyczne('Jan Khalib', 'BI', 'Dzadua', '2019')
print(utwory)
    