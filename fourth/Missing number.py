##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#here the input is given like integers in that some are missing
#and the output should be like the missing integers
#Sample Input
##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

s = list(map(int, input().split()))
num = sorted(s,reverse=True)
n = len(s)
for i in range(-1,-n-1,-1):
    if i not in s:
        print(i)
        break
