#here in this matrix th user give the input 3
#and the output is 3*3 matrix
#the input is given like this
#1 2 3
#2 3 1
#3 1 2
#the output should be True else False

m = int(input())
matrix = []
for i in range(m):
    each_row = list(map(int,input().split()))
    matrix.append(each_row)
#print(matrix)

count = 0
for j in range(m):
    set_numb = set(range(1,m+1))
    if set(matrix[j])==set_numb:
        count += 1
if count == m:
    print("True")
else:
    print("False")


