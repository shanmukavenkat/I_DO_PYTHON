##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
# here the input will be 3
# 4 1 3
# 2 5 6
# 1 2 3
# and the output will be 1st and 2nd and 3rd row of diagonal element
# that os 2 + 1 + 6 + 2 = 11
##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--


n = int(input())
mat = []
for i in range(n):
    m = list(map(int,input().split()))
    mat.append(m)
s = 0
for i in range(n):
    for j in range(n):
        if (i == j) or (i+j== n-1):
            continue
        else:
            s += mat[i][j]

print(s)
