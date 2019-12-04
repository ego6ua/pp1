class University():
    # konstruktor obiektu (metoda __init__)
    def __init__(self):
        # cechy obiektu (pola)
        self.name = 'UEK'
        # zachowania obiektu (metody)
    def print_name(self):
        print(self.name)
    
    def set_name(self, new_name):
        self.name = new_name
        print(self.name)
        
    def print_fullname(self, fullname):
        self.name = fullname
        print(self.name)
    
    def set_fullname(self, set_fullname):
        self.name = set_fullname
        print(self.name)
        
un = University()
un.print_name()
un.set_name('Uniwersytet w Krakowie')
un.print_fullname('Uniwersytet Ekonomiczny w Krakowie')
un.set_fullname('Uniwersytet Ekonomiczny w Warszawie')
