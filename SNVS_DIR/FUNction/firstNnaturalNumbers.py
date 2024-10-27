## the natural ==>1 2 3 4 5 and there sum
def naturalNum(a):
    k = 0
    for i in range(1, a + 1):
        k = k + i
    return k

a = int(input())
print(naturalNum(a))
