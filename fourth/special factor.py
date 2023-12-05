##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

#Test Case If N  20 ,
#The factors of 20 are 1, 2, 4, 5, 10, 20 . Whereas the special
#factors are 2, 5 .
#The output should be 2 5.
##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--


def check_prime(a):
    if a<2:
        return False
    count = 0
    for i in range(2,a):
        if a%i == 0:
            count += 1
            break
    if count == 0:
        return True
    else:
        return False



n = int(input())
num = []
for i in range(1,n+1):
    if n%i == 0:
        num.append(i)
special = list(filter(check_prime, num))
print(*special)