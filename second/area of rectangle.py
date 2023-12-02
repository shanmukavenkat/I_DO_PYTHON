#You are given a matrix filled with X's and O's.
# Your task is to find the largest rectangle that contains only X's and return its area.
# If there are no Xs in the entire matrix, print 0.

#Approach
#To solve this problem, we will:
#1. Read the matrix from input.
#2. Check if a sub-matrix contains any O's.
#3. Find the maximum sub-matrix area that contains only X's.
#4. Get the maximum area of the rectangle.

#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#Step 1: Read the matrix
#We will create a function read_matrix(rows) to read the input matrix.
#The function takes the number of rows as input and returns the matrix.
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--


#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#Step 2: Check if sub-matrix contains zero
#We will create a function check_if_sub_matrix_contains_zero(matrix, i, j, k, l) to check
#if a sub-matrix contains any O's. The function takes the matrix,
# the starting row i, the starting column j, and the dimensions of the sub-matrix k and l as inputs.
# It returns True if the sub-matrix contains any O's, otherwise False.
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#Step 3: Get maximum sub-matrix area
#We will create a function get_max_sub_matrix_area(matrix, rows, columns, i, j) to find the maximum sub-matrix area
# that contains only X's. The function takes the matrix, the number of rows,
# the number of columns, the starting row i, and the starting column j as inputs.
# It returns the maximum sub-matrix area.
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--


#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#Step 4: Get maximum area of rectangle
#We will create a function get_max_area_of_rectangle(matrix, rows, columns)
# to find the maximum area of the rectangle containing only X's.
# The function takes the matrix, the number of rows, and the number of columns as inputs.
# It returns the maximum area of the rectangle.
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--


def read_matrix(rows):
    matrix = []
    for i in range(rows):
        row = input().split()
        matrix.append(row)
    return matrix


def check_if_sub_matrix_contains_zero(matrix, i, j, k, l):
    for m in range(0, k + 1):
        for n in range(0, l + 1):
            if (matrix[i + m][j + n] == "O"):
                return True
    return False


def get_max_sub_matrix_area(matrix, rows, columns, i, j):
    max_sub_matrix_area = 0
    for k in range(0, rows - i):
        for l in range(0, columns - j):
            is_sub_matrix_contains_zero = check_if_sub_matrix_contains_zero(matrix, i, j, k, l)
            # If the submatrix does not contain zero, then it is possible that the submatrix may contain the maximum area
            if not is_sub_matrix_contains_zero:
                # Here, (k + 1) * (l + 1) provides the newly discovered sub matrix area
                max_sub_matrix_area = max(max_sub_matrix_area, (k + 1) * (l + 1))
    return max_sub_matrix_area


def get_max_area_of_rectangle(matrix, rows, columns):
    max_area_of_rectangle = 0
    for i in range(rows):
        for j in range(columns):
            if (matrix[i][j] == "X"):
                # When the current element is "X", start finding the maximum submatrix area
                # on the bottom right that starts with the current element.
                max_sub_matrix_area = get_max_sub_matrix_area(matrix, rows, columns, i, j)
                max_area_of_rectangle = max(max_area_of_rectangle, max_sub_matrix_area)
    return max_area_of_rectangle


def main():
    rows, columns = map(int, input().split(" "))
    matrix = read_matrix(rows)
    max_area_of_rectangle = get_max_area_of_rectangle(matrix, rows, columns)
    print(max_area_of_rectangle)


main()

#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#def get_matrix_area_of_rectangle(matrix, rows, columns):
#    max_area_of_rectangle = 0
#   for i in range(rows):
#       for j in range(columns):
#           if (matrix[i][j] == "X"):
#                for k in range(0, rows - i):
#                    for l in range(0, columns - j):
#                        found = True
#                        for m in range(0,k+1):
#                           for n in range(0,l+1):
#                                if matrix[i+m][j+n] != "X":
#                                   found = False
#                       if found:
#                            max_area_of_rectangle = max(max_area_of_rectangle, (k+1)*(l+1))
#   return max_area_of_rectangle


#def read_matrix(rows):
#    matrix = []
#    for i in range(rows):
#        rows = input().split()
#        matrix.append(rows)
#    return matrix

#def main():
#    rows, columns = map(int, input().split())
#    matrix = read_matrix(rows)
#    max_area_of_rectangle = get_matrix_area_of_rectangle(matrix, rows, columns)
#    print(max_area_of_rectangle)

#main()
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--