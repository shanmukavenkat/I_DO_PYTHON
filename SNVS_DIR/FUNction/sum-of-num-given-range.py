def sumofnum(a,b):
    c = 0
    for i in range(a,b+1):
        c = c+i
    return c

a = int(input())
b = int(input())
print(sumofnum(a,b))