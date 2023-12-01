#Test Case: 1 If the given numbers 25
#Where, X1 = 2 and pow1 = 5.
#Therefore, Sum = 2
#5 32.
#The output should be 32.
#Test Case: 2 If the given numbers  132 301
#Where,
#X1  13 and pow1  2.
#X2  30 and pow2  1.
#Therefore, Sum = 13
#2 + 30
#1 = 169 30 = 199.
#The output should be 199.

nums = input().split()

sum_of = 0
for each_num in nums:
    if len(each_num) ==1:
        pass
    else:
        power = each_num[-1]
        number = each_num[:-1]

        sum_of_power = int(number)**int(power)
        sum_of += sum_of_power
print(sum_of)