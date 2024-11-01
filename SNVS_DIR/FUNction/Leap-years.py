n = int(input("Lower Year:"))
p = int(input("Higher Year:"))
k = []
for i in range(n,p+1):
    if(i%4 ==0 and i%100 !=0 ) or (i%400 ==0):
        k.append(i)


print(*k)
