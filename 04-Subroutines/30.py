from random import randrange
def liczby():
    x = randrange(1,51)
    return x
p=0
n=0    
for i in range(1000):
    if liczby()%2==0:
        p+=1
    else:
        n+=1
parzyste=p/10
nieparzyste=n/10
print(f'Dla 1000 liczb losowych z przedziału <1,50>:\nLiczby parzyte: {parzyste}%\nLiczby nieparzyste: {nieparzyste}%')