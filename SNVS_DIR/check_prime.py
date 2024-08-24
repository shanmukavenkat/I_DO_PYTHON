n = int(input())

if n == 1:
    print("it is not a prime")

if n > 1:
    for i in range(2,n):
        if n % i == 0:
            print("it is not a prime")
            break
    else:
        print("it is a prime")