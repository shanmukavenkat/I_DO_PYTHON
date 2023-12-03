##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
# in this input will be string containing numbers
#For example, if the actual sentence is It is a 3days 4nights holiday trip .
#The numbers in the sentence are 3 and 4. After arranging them in
#decreasing order, the output looks like It is a 4days 3nights holiday trip .
#Sample Input
#It is a 3days 4nights holiday trip
#Sample Output
#It is a 4days 3nights holiday trip
##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--


string = input()
num = ""
for i in string:
    if i.isdigit():
        num += i
    else:
        num += " "
num = num.split()
num = list(map(int, num))
number = sorted(num,reverse=True)

if len(num) == 0 or len(num) == 1:
    print(string)
else:
    res = ""
    i = 0
    j = 0
    k = len(string)
    while j < k:
        if string[j].isdigit():
            if string[j].isdigit() and (j == 0 or (not string[j-1].isdigit())):
                res += str(number[i])
                m = len(str(number[i]))
                i += 1
                j += 1
            else:
                j += 1
        else:
            res += string[j]
            j += 1
    print(res)



















