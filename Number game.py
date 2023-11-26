#2 3 3 4 5 6 7 8
#3
#now we have to remove the first 3 elements from the list
#then print the remaining numbers
#output: 4 5 6 7 8
#output: 2 3 3 4 5
##these like the output should be

def convert_string(num):
    output_str = ""
    for i in num:
        output_str += str(i)+" "
    return output_str
nums = list(map(int,input().split()))

random_num = int(input())
first_num = nums[random_num:]
second_num = nums[:-random_num]
print(first_num)
print(second_num)

