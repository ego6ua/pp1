import re
def nie_powtarza(tab):
    tab2 = []
    for i in tab:
        x = re.findall(str(i), str(tab))
        if (len(x)==1):
            tab2.append(i)
    return tab2
tablica = [1, 2, 2, 2, 3, 4, 5, 6, 6, 7, 7, 8, 9]
print(nie_powtarza(tablica))