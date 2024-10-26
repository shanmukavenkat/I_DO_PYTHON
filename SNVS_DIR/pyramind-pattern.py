k = int(input("Enter the number of rows: "))
for i in range(1, k + 1):
    print("  " * (k - i) + f"{i} " * (2 * i - 1))

n = int(input())
for i in range(n):
    spaces = ("  ") * (n - i - 1)
    string = (str(i + 1) + " ") * ((2 * i) + 1)
    print(spaces + string)