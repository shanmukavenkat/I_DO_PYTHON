#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#You have given a positive number N and asked to convert that
#number N into a single digit by repeatedly adding its digits until it
#becomes a single digit.
#Repeatedly add the digits of the given number 545 until it
#becomes a single digit like as shown below
#Add the digits of the given number:
#Repeat the process and add the digits of the result:
#5 + 4 + 5 = 14
#1 + 4 = 5
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--


n = str(int(input()))
m = len(n)
while m > 1:
    string = list(n)
    num = sum(list(map(int,string)))
    n = str(num)
    m = len(n)
print(int(n))
