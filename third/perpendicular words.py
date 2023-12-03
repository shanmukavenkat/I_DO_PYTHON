##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#here the given input is cat bat vin
#and the output is
# c b v
# a a i
# t t n
# here we can observe that the output will be in the horizontal way
##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--






s = input().split()
k = max(len(i) for i in s)
res = [""]*k
for i in range(k):
    for word in s:
        if len(word) > i:
            res[i] += word[i]
        else:
            res[i] += " "
for i in res:
    print(i)