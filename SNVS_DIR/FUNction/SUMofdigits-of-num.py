def sumofNUm(a):
    k = 0
    for i in a:
        m = int(i)
        k = k+m
    return k

n = input()
the_answer = sumofNUm(n)
print(the_answer)