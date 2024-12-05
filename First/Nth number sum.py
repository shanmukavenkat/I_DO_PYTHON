#4 12
#7 3 10 4 5 8 4 9 6 9 10 1 4
#output should be 4+9+1=14

num = input().split()

n = int(num[0])
m = int(num[1])

num_list = list(map(int,input().split()))
sum_of = 0
for i in range(1,m+1):
    if i % n == 0:
        sum_of += num_list[i-1]

print(sum_of)

