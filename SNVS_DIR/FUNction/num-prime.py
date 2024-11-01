num = int(input("Enter Number:"))

if num >1:
    for i in range(2,num):
        if(num%i == 0):
            print("It is not a prime")
            break
    else:
        print("IT is a prime")

else:
    print("It is not a prime")

