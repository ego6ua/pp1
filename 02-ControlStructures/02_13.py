x = 5
y = 2
z = (f"P({x},{y})")
if x>0 and y>0:
    print(f'Punkt {z} znajduje się w pierwszej ćwiartce układu współrzędnych')
elif x<0 and y>0:
    print(f'Punkt {z} znajduje się w drugiej ćwiartce układu współrzędnych')
elif x<0 and y<0:
    print(f'Punkt {z} znajduje się w trzeciej ćwiartce układu współrzędnych')
else:
    print(f'Punkt {z} znajduje się w czwartej ćwiartce układu współrzędnych')