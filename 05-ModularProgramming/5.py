import statistics
tab = [21600, 4350, 3920, 5590, 3250, 4010]
a = sum(tab)/len(tab)
b = statistics.median(tab)
#c = 
print(f'Średnia artymetyczna: {int(a)}')
print(f'Mediana: {int(b)}')