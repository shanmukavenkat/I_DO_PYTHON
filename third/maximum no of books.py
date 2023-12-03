##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#The first line of input is a positive integer T that represents the number of shops.
#The following lines represent the details of the T shops.
#Each set of two consecutive lines represents the details of a shop.
#The first line of each set contains two space-separated integers B andP .
#The second line of each set contains B space-separated integers
#output
#The output should be T lines.
#Each line contains an integer that represents the maximum number of
#books that can be bought in each shop.

#Explanation
#Given P  600 and B  120, 140, 110, 180, 120, 110
#With a pocket money of 600 , we can buy the books at index 0, 1,
#2, 4, 5 , whose sum is 120+140+110+120+110 is equal to P .
#Given P  300 and B= [ 120 110 1300 130]
#With pocket money of 300 , we can buy the books at index 0, 1
#whose sum is 120+110 and is less than P .
#Given P  100 and B = [220 1000 500 2000]
#With pocket money of 100 , we can't buy any book.
#So, the output should be
#5
#2
#0
##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

def maximum_books(n,p,m):
    s = 0
    count = 0
    for i in m:
        s += i
        if s<=p:
            count += 1
        else:
            break
    return count

n = int(input())
for i in range(n):
    books, pocket = map(int,input().split())
    m = sorted(list(map(int,input().split())))
    result = maximum_books(books,pocket,m)
    print(result)
