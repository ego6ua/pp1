def reverse(tab):
    print('Tablica: ', end='')
    for i in tab:
        print(i, end=' ')
    print('\nTablica odwrocona: ', end='')
    for x in reversed(tab):
        print(x, end=' ')
    
reverse([2, 5, 4, 1, 8, 7, 4, 0, 9])