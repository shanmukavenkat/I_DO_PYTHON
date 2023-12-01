#here the given input is 3
#so the 3x3 matrix is
# 1 2 3
# 4 5 6
# 7 8 9
#here the sum of upper triangle is 1+2+3+4+5+7 = 22
#here the sum of lower triangle is 3+5+6+7+8+9 = 38



a = int(input())
listing = []
for i in range(a):
    n = list(map(int,input().split()))
    listing.append(n)
sum_of_upper = []
for i in range(a):
    result = listing[i][:a-i]
    sum_of_upper.append(sum(result))
print(sum(sum_of_upper))

sum_of_lower = []
for i in range(1,a+1):
    result = listing[i-1][-i:]
    sum_of_lower.append(sum(result))
print(sum(sum_of_lower))