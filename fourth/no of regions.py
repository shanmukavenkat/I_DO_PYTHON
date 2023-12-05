##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#Given R=6 C=10
#and the matrix
#1 1 1 1 0 1 1 0 1 1
#1 0 0 0 0 0 0 1 1 1
#1 0 1 1 0 0 0 1 0 1
#1 0 1 1 0 1 0 1 1 1
#0 0 0 0 0 1 1 0 0 1
#0 0 0 0 1 1 1 0 1 0
#Different regions of this matrix are highlighted with different colors in
#the above image.

#As a region is a collection of ones interconnected horizontally or
#vertically, but not diagonally, the regions green, yellow, purple, red
#are not considered as single region as highlighted in the above
#image.
#Also, notice that the yellow region has a hole in it.

#As it can be observed from the image, there are a total of 6 regions
#(blue, green, yellow, purple, red, pink).
#So the output is 6 .

##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--


















def count_regions(matrix):
    rows,cols = len(matrix),len(matrix[0])
    regions = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                regions += 1
                stack = [(i,j)]
                while stack:
                    x,y = stack.pop()
                    if x < 0 or x >= rows or y < 0 or y >= cols or matrix[x][y]!= 1:
                        continue
                    matrix[x][y] = -1
                    stack.extend([(x-1,y),(x+1,y),(x,y-1),(x,y+1)])
    return regions
r,c = map(int,input().split())
mat = []
for i in range(r):
    m = list(map(int,input().split()))
    mat.append(m)
result = count_regions(mat)
print(result)
