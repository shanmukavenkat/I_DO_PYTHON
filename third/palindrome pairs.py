#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
# input : was it a car or a cat i saw
# word indices = (was ,saw) = (0,8) (a ,a)= (2,5) (a,a) = (5,2) (saw,was) =(8,0)
# output : 0 8
#          2 5
#          5 2
#          8 0
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

def check(s):
    return s == s[::-1]

l = list(input().split())
n = len(l)
pair = set()
for i in range(n):
    for j in range(n):
        string = l[i]+l[j]
        if check(string):
            if i!= j:
                pair.add((i,j))

order_pair = sorted(list(pair))
if len(order_pair)>0:
    for num in order_pair:
        print(*num)
else:
    print(-1)
