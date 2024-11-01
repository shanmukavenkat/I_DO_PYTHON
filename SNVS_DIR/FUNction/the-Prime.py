def theFunction(n):

    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True



the_num = int(input("Enter the NUM:"))
k = []


for ij in range(1,the_num+1):
    if theFunction(ij):
        k.append(ij)

print(*k)
