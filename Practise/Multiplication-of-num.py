def number(n):
    k = ""
    for i in range(1,11):
        k += f"{n} X {i} = {n*i}\n"
    return k

num = int(input())
print(number(num))