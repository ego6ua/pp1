import statistics
tab = [21600, 4350, 3920, 5590, 3250, 4010]
a = sum(tab)/len(tab)
b = statistics.median(tab)
c = statistics.pstdev(tab)
print(f'Średnia artymetyczna: {int(a)}')
print(f'Mediana: {int(b)}')
print(f'Odchylenie standardowe: {int(c)}')