##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#Test Case: Given S = Welcome to your first problem
# N = 5 ,
#Rotate the sentence by 5 letters towards the left without changing
#the length of the words and position of spaces in the original
#sentence.
#The output should be metoyou rf irst probl emWelco.
###---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--



s = input()
n = int(input())
index = []
res = ""
for i in range(len(s)):
    if s[i] == " ":
        index.append(i)
    else:
        res += s[i]
m = len(res)
rotate = n % m
word = res[rotate:]+res[:rotate]
j = 0
sent = ""
for i in range(len(s)):
    if i in index:
        sent += " "
    else:
        sent += word[j]
        j += 1
print(sent)
