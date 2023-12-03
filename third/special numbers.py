##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
# here the input will be  set of numbers
#21 503 256 550 86 979 281
#the output should be containing hte number start with the odd number
#12 503 256 550 86 979 128
##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

l = input().split()
res = []
for num in l:
    if (int(num[0])%2==1):
        res.append(num)
    else:
        k = True
        for i in range(len(num)):
            if int(num[i])%2==1:
                number = num[i:]+num[:i]
                res.append(number)
                k = False
                break
        if k:
            res.append(num)
print(*res)
