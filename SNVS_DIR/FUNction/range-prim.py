num = int(input())
num2 = int(input())

if num >1 and num2>1:
    k = []
    for i in range(num,num2+1):
        if(num%i == 0):
            print("it is not a prime")
    else:
        print("It is prime")
        k.append(i)
    print(k)

else:
    print("It is not prime")