def sqrt(number):
    x = 0
    while(x+1)*(x+1)<=number:
        x +=1
    return x

n = int(input())
print(sqrt(n))