###She/he knows that when the magnitude of an earthquake increases by
##1, the amount of energy multiplies by 32. Help Shreya in determining
##the intensity of earthquake A compared to earthquake B.
##Input Format: 4 6
##Output Format: powers of difference in input format which is 32power(6-4) = 1024

num_list = list(map(int,input().split()))
diff = abs(num_list[1]-num_list[0])
#print(diff)
print(32**diff)
