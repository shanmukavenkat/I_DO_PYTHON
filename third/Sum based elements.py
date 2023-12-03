#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#1. The code takes an integer `n` as input and constructs an `n x n` matrix by taking input for each element.
#2. It calculates the sum (`s`) of elements located on the main diagonal and secondary diagonal of the matrix.
#3. The final sum (`s`) is printed as the output.
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

n = int(input())
mat = []
for i in range(n):
    m = list(map(int,input().split()))
    mat.append(m)
s = 0
for i in range(n):
    for j in range(n):
        if (i == j) or (i+j == n-1):
            s += mat[i][j]
print(s)