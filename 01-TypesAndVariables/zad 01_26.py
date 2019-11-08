wzrost = int(input("Podaj wzrost w cm "))
waga = int(input("Podaj wagę w kg "))
bmi = waga/((wzrost/100)**2)
if bmi < 18.5:
    print(f"Wskaznik BMI {bmi} (niedowaga)")
elif bmi <= 24.9:
    print(f"Wskaznik BMI {bmi} (prawidlowa)")
elif bmi <= 29.9:
    print(f"Wskaznik BMI {bmi} (nadwaga)")
elif bmi > 30:
    print(f"Wskaznik BMI {bmi} (otyłość)")
else:
    print(f"Wskaznik BMI {bmi} (otyłość)")