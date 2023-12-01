#The input will be a single line containing space-separated integers
#representing S and T
#Output
#The output should be a single line containing an integer representing
#the count of triplets of non-negative integers (a, b, c) satisfying the
#above conditions.
#Explanation
#Test Case: If the given S  1 and T  0
#Possible triplets which are satisfying the above given conditions are
#0, 0, 0 , 0, 1, 0 , 0, 0, 1 and 1, 0, 0 .
#The output should be 4.


nums = input().split()


S = int(nums[0])
T = int(nums[1])
triple_count =0
for a in range(S+1):
    for b in range(S+1):
        for c in range(S+1):
            #print(a,b,c)
            if a+b+c <= S and a*b*c <= T:
                triple_count += 1

print(triple_count)