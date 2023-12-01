#here we have to print the alphabets according to the index given by the user

num_index = list(map(int,input().split()))
alphabets_list = "abcdefghijklmnopqrstuvwxyz"

result = " "
for i in num_index:
    result += alphabets_list[i-1]
print(result)