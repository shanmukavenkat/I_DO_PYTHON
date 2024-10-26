a = int(input())

for i in range(a):
    print(" "*(a-i), end=" ")  # Print spaces to align the pattern
    for j in range(a-i, 0, -1):  # Decreasing numbers in each row
        print(j, end=" ")
    print()  # Newline after each row
