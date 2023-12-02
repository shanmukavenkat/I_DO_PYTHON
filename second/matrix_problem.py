#If the given M = 2 and N = 3, the matrix is as follows:
#1 0 1
#0 2 0
#The position of zeroes are (0, 1), (1, 0), and (1, 2). Replace them with the sum of
#neighboring elements.
#Positions	Neighbour Elements	Sum
#(0, 1)-------->1 + 2 + 1----------->4
#(1, 0)-------->1 + 2------------->3
#(1, 2)-------->1 + 2------------->3
#All the other elements in the corresponding row and column of
# those identified zeroes should be set to 0
#(excluding the elements which were previously zeroes).
#The output should be,
#0 4 0
#3 0 3






import copy


m,n = map(int,input().split())
matrix = []
for i in range(m):
    line = list(map(int,input().split()))
    matrix.append(line)

duplicate_matrix = copy.deepcopy(matrix)


for row in range(m):
    for col in range(n):
        if matrix[row][col] == 0:
            duplicate_matrix[row] = [0]* n
            for i in range(m):
                duplicate_matrix[i][col] = 0


for row in range(m):
    for col in range(n):
        if matrix[row][col] == 0:
            top_val = matrix[max(row-1,0)][col]
            right_val = matrix[row][min(col+1,n-1)]
            bottom_val = matrix[min(row+1,m-1)][col]
            left_val = matrix[row][max(col-1,0)]
            sum_of_value = top_val+right_val+bottom_val+left_val
            duplicate_matrix[row][col] = sum_of_value

for i in duplicate_matrix:
    print(*i)


