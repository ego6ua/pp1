class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = ['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox']
        self.poziom_głośności = 0
        
    def on(self):
        self.is_on = True
    
    def off(self):
        self.is_on = False
        
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
        
    def set_channels(self, channels_list):
        self.channels = list(channels_list)
        
    def zwiększyć_głośność(self, zw_poziom_g):
        self.poziom_głośności += zw_poziom_g
        
    def zmniejszyć_głośność(self, zm_poziom_g):
        self.poziom_głośności -= zm_poziom_g
        
    def show_channels(self):
        print('=' * 17)
        print('LISTA KANAŁÓW TV')
        x = 1
        for i in self.channels:
            print(str(x) + '.' + i)
            x += 1
        print('=' * 17)
    
    def show_status(self): #print(f'Poziom głośności: {self.poziom_głośności}')
        if self.is_on and self.channel_no <= 5:
            print('Odbiornik TV jest załączony, kanał ' + '(' + self.channels[self.channel_no - 1] + ')')
            if self.poziom_głośności >= 0 and self.poziom_głośności <= 10:
                print(f'Poziom głośności: {self.poziom_głośności}')
            elif self.poziom_głośności < 0:
                print(f'Poziom głośności: 0')
            elif self.poziom_głośności > 10:
                print(f'Poziom głośności: 10')
                
        elif self.is_on and self.channel_no > 5:
            print('Odbiornik TV jest załączony, !!! kanał nie istnieje !!!')
            
        else:
            print('Telewizor jest wyłączony')
        
        
tv = TV()
tv.on()
tv.set_channel(5)
#tv.zwiększyć_głośność(10)
#tv.zmniejszyć_głośność(3)
tv.show_channels()
tv.show_status()