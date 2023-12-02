#If the given M = 4 and N = 4, the matrix is as follows:
# 1 2 3 4
# 5 6 7 8
# 4 3 2 1
# 8 7 6 5
# If K = 2, the sub-matrix is as follows:
#Delete 2 rows from both the top and the bottom of the matrix.
#Delete 2 columns from both the left and the right of the matrix.
#Then, the resulting matrix will no longer contain any elements.
#The output should be 0.





m,n = list(map(int,input().split()))
e = []
for i in range(m):
    matrix = list(map(int,input().split()))
    e.append(matrix)
k = int(input())
sub = e[k:m-k]
if len(sub)<=0:
    print("[]")
else:
    empty_list = []
    for j in (sub):
        r = j[k:n-k]
        empty_list.extend(r)
    result = 1
    for res in empty_list:
        result *= res
    print(result)