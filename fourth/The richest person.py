##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
# input N = 4
# John Cena 1000
# Jane 2000
# Jack 4000
# Tom 400
# Both Jack and Tom have the highest net income. As jack is
# lexicographically smaller than tom and found at index 2 , the
# output is Jack 2 .
#----------------------------------------------------------------------------------------
#For N  4 , the input is:
#John Cena 1000
#Patel 1500
#Mar K 1000
#Mark 500
#mark (1000  500) and patel (1500) both earn the same. So, we
#have a tie here. In case of tie choose the name that is smallest
#lexicographically which is mark( m comes before p in
#dictionary). The first index of the mark in the given input is Mar K
#which is at index 2 .
#So the output is Mar K 2 .

##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

n = int(input())
book = []
for i in range(n):
    m = input().split()
    book.append(m)
rich = {}

for name in book:
    salary = int(name.pop())
    s = "".join(name)
    person = s.lower()
    if person in rich:
        value = rich[person]
        rich[person] = value + salary
    else:
        rich[person] = salary

k = list(rich.items())
k.sort(key=lambda x:x[1],reverse=True)
salaries = list(rich.values())
maximum = max(salaries)
count = salaries.count(maximum)
if count == 1:
    unique = k[0][0]
else:
    res = []
    for a,b in rich.items():
        if b == maximum:
            res.append(a)
    res.sort()
    unique = res[0]
i = 0
for rock in book:
    rich_person = " ".join(rock)
    s = "".join(rock)
    person = s.lower()
    if unique == person:
        print(rich_person+" "+str(i))
        break
    i += 1