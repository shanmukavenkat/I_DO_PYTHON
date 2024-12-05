#1 2 2 3 3 3 4 5 6
#2
#0 2
#1 4
#the output 1+2+2=5
#the output 1+2+2+3+3+3+4=18
def add_all_num(input_list ,input_range):
    start = int(input_range[0])
    end = int(input_range[1])
    sum_of =0
    for i in range(start,end+1):
        if i in input_list:
            count_of = input_list.count(i)
            sum_of += (i*count_of)
    return sum_of



input_list= list(map(int,input().split()))
num = int(input())
for i in range(num):
    input_range = input().split()
    result = add_all_num(input_list,input_range)
    print(result)
