t = [32, 16, 5, 8, 24, 7]
with open('Tablica.txt','w') as file:
    for i in t:
        file.write(f'{str(i)}\n')
        
file.close()