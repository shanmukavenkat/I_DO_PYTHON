##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
# here the input will be string and in that string
# input :- I am 5 years 11 months and 8 days old
# output:- I am 5 years 8 months and 11 days old
# here the integers should be arranged in ascending order (increasing order)
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
number = sorted(num)

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
