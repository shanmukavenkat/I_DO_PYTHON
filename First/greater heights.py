#here the input which will give 5 students and 2 rows
#here the input like 5 2
#here the 5 students data will be given  like 321 456 789 654 159 357 4862
#here the two rows will be given like
#456
#789
#here the output should give considering the numbers
#in the first row and second row
#here each data of students are compared with the first row and second row
#and printing how many students data is more than the first row and second row
#here the output should be 3
#here the output should be 2



nums = input().split()

no_of_students = int(nums[0])
no_of_queries = int(nums[1])

no_of_stu = list(map(int,input().split()))

no_of_queries_list = []

for i in range(no_of_queries):
    query = int(input())
    no_of_queries_list.append(query)

for each_query in no_of_queries_list:
    count = 0
    for each_stu in no_of_stu:
        if each_stu >= each_query:
            count += 1
    print(count)







