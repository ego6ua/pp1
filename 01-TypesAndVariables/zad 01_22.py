a = int(input("wpisz bok a:"))
b = int(input("wpisz bok b:"))
c = int(input("wpisz bok c:"))
p = (a+b+c)/2
import math
f = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"Pole trójkata wynosi {f}")