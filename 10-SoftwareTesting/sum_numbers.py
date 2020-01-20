# Sumuje liczby nturalne parzyste z przedziału <from_n,to_n>
def sum_even(from_m,to_n):
    sum = 0
    if from_m<0:
            from_m = 0
    if to_n<0:
        to_n=0 
    for i in range(from_m,to_n+1):
                   
        if i%2 == 0: # liczba parzysta
            sum += i
    return sum

def main():
    m = 2
    n = 8
    print(f"Suma liczb naturalnych parzystych z przedziału <{m},{n}> wynosi {sum_even(m,n)}")

if __name__ == "__main__":
    main()