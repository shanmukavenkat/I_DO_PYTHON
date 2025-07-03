string = input()
number = int(input())

length_number = len(string)

if length_number % number !=0:
    print("Invalid partitions")
else:
    partsize = length_number// number
    for i in range(0, length_number, partsize):
        parts = [string[i:i + partsize] for i in range(0, length_number, partsize)]
        print(" ".join(parts))

