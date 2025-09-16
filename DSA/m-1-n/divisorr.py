a = int(input("enter the input number: "))
divisors = []
for i in range(1,a+1):
    if a%i == 0:
        print("the divisors in the normal form",i)
        divisors.append(i)
        print("the divisors in the list form",divisors)

