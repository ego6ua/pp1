
try:
    with open('NoEducation.txt', 'r') as file:
        print(file.read())
except:
    print('Nieprawidlowa nazwa pliku lub nie ma takiego pliku')