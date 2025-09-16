a = int(input("enter the number: "))
b = int(input("enter the number to divide it and check the divisor: "))
"print(a%b)"
for i in range(1, a+1):
    if a%i == 0:
        print(i)
    else:
        print("not a divisor")