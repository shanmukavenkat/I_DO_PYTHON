def missing_number(arr):
    the_number = len(arr)+1
    the_sum = the_number*(the_number+1)//2
    actual_sum = sum(arr)
    return the_sum - actual_sum

the_number = list(map(int,input().split()))
print(missing_number(the_number))