#If the given N  3 and S  13 12 11
#Score of student 1 is 13 .
#Score of student 2 is 12 .
#Score of student 3 is 11 .
##The number of people who took the viva after student 1 and scored
#less than 13 is 2 ( 12 , 11 ).
#The number of people who took the viva after student 2 and scored
#less than 12 is 1 ( 11 ).
#The number of people who took the viva after student 3 and scored
#less than 11 is 0 .
#The output should be 2 1 0.
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#If the given N = 4 and S = 1 2 3 4

#Score of student 1 is 1.
#Score of student 2 is 2.
#Score of student 3 is 3.
#Score of student 4 is 4.

#The number of people who took the viva after student 1 and scored less than 1 is 0.
#The number of people who took the viva after student 2 and scored less than 2 is 0.
#The number of people who took the viva after student 3 and scored less than 3 is 0.
#The number of people who took the viva after student 4 and scored less than 4 is 0.

#The output should be 0 0 0 0



def vi_scores(list_a,num):
    start_index = 0
    count_list = []
    for each in range(start_index,num):
        new_list = list_a[start_index:]
        maximum_num = list_a[start_index]
        count = 0
        for i in new_list:
            if maximum_num > i:
                count += 1
        count_list.append(count)
        start_index += 1
    print(*count_list)


num = int(input())
list_a = list(map(int,input().split()))
vi_scores(list_a,num)
