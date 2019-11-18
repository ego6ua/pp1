'''f = open('C:/Users/s-115-23/Desktop/pp1/05-ModularProgramming/employees.csv', 'r')
print(f.read())'''
import csv
import statistics
with open('employees.csv', newline='') as f:
    x = 1
    wiek = []
    reader = csv.reader(f)
    print('#    ', end = '')
    for row in next(reader):
        print(f'%-15s'%row.upper(), end = '')
    print(' ')
    print('='*70)
    for row in reader:
        print(f'%-3d %-15s %-15s %-15s %s'%(x, row[0], row[1], row[2], row[3]))
        x+=1
        wiek.append(int(row[2]))
    print(statistics.mean(wiek))
    #print(sum(int(row[2]))/lenint(int(row[2])))