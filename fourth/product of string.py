###---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><-
#Test Case: If the given string S is 123a4 ,
#ASCII value of a is 97 .
#Product of digits of ASCII value of a is
#9 x 7 = 63
#Therefore the product of characters is
#1 x 2 x 3 x 63 x 4 = 1512
#The output should be 1512.
###---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><-

def product_of_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

s = input()
p = 1
for i in s:
    if i.isdigit():
        p *= int(i)
    else:
        num = ord(i)
        k = list(str(num))
        n = list(map(int, k))
        res = product_of_list(n)
        p *= res
print(p)