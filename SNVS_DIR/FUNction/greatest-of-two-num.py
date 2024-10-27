def great_numbers(a,b,c):
    if(a>b and a>c and b>c):
        return a
    elif(b>a and b>c and a>c):
        return b
    elif(c>a and c>b and b>a):
        return c

a,b,c = map(int,input().split())
print(great_numbers(a,b,c))