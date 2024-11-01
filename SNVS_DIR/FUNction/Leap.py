def LeapYear(n):
    if (n%4 == 0 and n%100 != 0) or (n%400 ==0):
        return "It is a Leap Year"
    else:
        return "It is not a Leap year"


year = int(input())
k = LeapYear(year)
print(k)
