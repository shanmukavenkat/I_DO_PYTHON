##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
# in the input 2
# i slove
# can this
# the output is ------> i can
#                       slove this
##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--


n = int(input())
mat = []
for i in range(n):
    m = input().split()
    mat.append(m)
k = max(len(i) for i in mat)
l = [""]*k
for i in range(k):
    for word in mat:
        if len(word) > i:
            l[i] += word[i]
for j in l:
    print(j)