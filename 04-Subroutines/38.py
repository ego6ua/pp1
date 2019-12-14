napis = "Krakow - stolica Polski"
import re
def litery(n):
    dli = ''
    for i in napis:
        x = re.findall('[A-Z]', napis)
    dli += str(x)
    return dli
print(litery(napis))

'''import re
def litery(a):
    litery_tab=re.findall("[A-Z]",a)
    ciag=""
    for i in litery_tab:
        ciag+=i
    return ciag
napis="Lorem Ipsum"    
print(f"Ciąg wielkich liter:{litery(napis)}")
'''
    
    
    
