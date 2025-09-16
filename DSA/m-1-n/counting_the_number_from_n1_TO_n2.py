a = int(input())
b = int(input())
count = 0
for i in range(a, b+1):
    for num in str(i):
        count += int(num)
print(count)



