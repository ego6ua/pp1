class Student():
    numer = 100000
    
    def __init__(self, imie, nazwisko, kierunek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kierunek = kierunek
        self.album = Student.numer
        
    def __str__(self):
        return f'{self.imie} {self.nazwisko} ({self.album}), {self.kierunek}, UEK Krakow'
student = Student('Ivan', 'Kudybyn', 'Informatyka stosowana')
print(student)
    