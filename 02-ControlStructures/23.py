ocena = input(int('Podaj ocenę: '))
tab = ['celujący', 'bardzo dobry', 'dobry', 'dostateczny', 'mierny', 'niedostateczny']
for i in tab:
    if ocena == i+4:
        print(i+4)