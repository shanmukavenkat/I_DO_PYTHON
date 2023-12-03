##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#Input
#The input will be a single line containing a sentence.
#
#Output
#The output should be multiple lines, each line containing a valid
#unique combination of two words. The words in each line should be
#lexicographical order and the lines as well should be in
#lexicographical order. A valid combination will not contain the words
#that appear adjacent in the given sentence. Print No Combinations if
#there are no valid combinations.

#Explanation
#For example, if the given sentence is python is a programming
#language , the possible unique combination of two are (a, is), (a,
#language), (a, programming), (a, python), (is, language), (is,
#programming), (is, python), (language, programming), (language,
#python), (programming, python). Out of these the combinations, (a,
#is), (a, programming), (is, python), (language, programming) are not
#valid as they contain words that are adjacent in the given sentence.
#So the output should be
#a language
#a python
#is language
#is programming
#language python
#programming python
#
#
#
#for example :- raju always plays cricket
#output :- always cricket
#          cricket raju
#          plays raju
##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

from itertools import combinations

comb_set = set()
s = input().split()
n = len(s)
comb = combinations(s,2)
for i in comb:
    comb_set.add(tuple(sorted(i)))
i,j = 0,1
adj_set = set()
while i<n and j<n:
    adj_set.add((s[i],s[j]))
    adj_set.add((s[j],s[i]))
    i+=1
    j+=1
unique_pair = comb_set -adj_set
num = sorted(list(unique_pair))
if len(num)>0:
    for i in num:
        print(*i)
else:
    print("No Combinations")