##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#here the input will be given like ---> Welcome to your exam
# and another input is given like ---> 6
# here the string which is containing the word length of 6 should be removed
# it has to form remaining sentence to get the length 6
# processing the input
# Sample Input Welcome to your exam
# 6
# --------------------------------------------------|
# | word 1 --------------------word 2 |
# | to-------------------------your   |
# | to-------------------------exam   |
# | exam-----------------------to     |
# | your-----------------------to     |

# Sample Output
#examto
#toexam
#toyour
#yourt
##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

train = input().split()
n = int(input())
res = set()
for i in range(len(train)):
    for j in range(len(train)):
        if i == j:
            continue
        else:
            word = train[i]+train[j]
            if len(word) == n:
                res.add(word)


sent = list(res)
sent.sort()
for num in sent:
    print(num)