
##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#In the example, the number is 17 . The closest number that has all
#even digits in it is 20 . So the output should be 20 .
#In example two, the number is 33 . The closest number that has
#all even digits in it is 28 . So the output should be 28 .
#Sample Input 1
#17
#Sample Output 1
#20
##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

def even(i):
    if int(i) % 2 == 0:
        return True
    else:
        return False


def check_number(num):
    t = list(str(num))
    q = list(map(even, t))
    number = all(q)
    return number


s = int(input())
a = s
b = s
k = True
while k:
    a += 1
    b -= 1
    if check_number(abs(b)):
        print(b)
        k = False
        break
    if check_number(abs(a)):
        print(a)
        k = False
        break
