#here the user will give how many numbers he want to enter
#if user enter 3
#then taken like given below
#3
#2 3 4
#4 5 6
#9 8 7
#among these three the highest sum of scores should be printed
#here the output should be 9+8+7=24 then 9 8 7 should be printed

num = int(input())

actual_list = []

for i in range(num):
    num_list = list(map(int,input().split(",")))
    actual_list.append(num_list)

group_with_highest_score = actual_list[0]

for each_group in actual_list:
    if sum(each_group)>sum(group_with_highest_score):
        group_with_highest_score = each_group

##wecan print the list into separate numbers using new method
##print(*group_with_highest_score)

output_string = ""
for i in group_with_highest_score:
    output_string += str(i)+" "

print(output_string.strip())
