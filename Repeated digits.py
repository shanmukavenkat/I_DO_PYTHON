#Test Case: If the given N = 212311
#In this number, digits 1 and 2 are repeated single-digit integers.
#The count of repeated single-digit integers in the given number is 2.
#The output should be 2.
#Sample Input 1
#212311
#Sample Output 1
#2

nums = input()

rep_num = []
for i in nums:

    if nums.count(i) > 1 and i not in rep_num:
        rep_num.append(i)

final_output = len(rep_num)
print(final_output)
