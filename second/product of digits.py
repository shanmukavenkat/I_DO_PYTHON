#here the input will be 1234
#and the result will be 1*2*3*4 = 24
#the result will be 24
#if input 02 have given the result will be 2



numbers = int(input())

nums_list = list(map(int,str(numbers)))

product = 1
for i in nums_list:
    product *= i
print(product)