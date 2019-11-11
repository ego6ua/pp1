n = str(input('Podaj nr rachunku bankowego: '))
#num = n[0:2][3:6][7:10][11:14][15:18][19:22][23:26]
a = n[0:2]
b = n[2:6]
c = n[6:10]
d = n[10:14]
e = n[14:18]
f = n[18:22]
g = n[22:26]
z = a+' '+b+' '+c+' '+d+' '+e+' '+f+' '+g
print(f'Nr rachunku: {z}')
