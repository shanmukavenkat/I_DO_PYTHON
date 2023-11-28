#given input  2 2 3 3 3 4 5 5
#output should print the single entry 1
#output 4
nums_list = list(map(int,input().split()))

length = len(nums_list)
for i in range(length):
    count = nums_list.count(nums_list[i])
    if count == 1:
        print(nums_list[i])
        break