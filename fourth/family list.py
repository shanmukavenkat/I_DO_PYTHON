###---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><-
#Given the number of test cases T = 1

#If the given N = 3 and  S = cat bat rat,

#To obtain the 2nd word bat from the 1st word cat, the letter c should be changed to b.

#To obtain 3rd word rat from the 2nd word bat, the letter b should be changed to r.

#As all the words are obtained from its previous words, the output should be Family.

###---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><-





def belongs_to_family(a, words):
    previous = words[0]
    res = [True]+[False]*(a-1)
    for i in range(1,len(words)):
        current = words[i]
        if len(current) == len(previous):

            count = 0
            for j in range(len(current)):
                if current[j] != previous[j]:
                    count += 1
            if count == 1:
                previous = current
                res[i] = True
        elif len(current) == len(previous)+1:

            for j in range(len(current)):
                if current[:j]+current[j+1:] == previous:
                    previous = current
                    res[i] = True
                    break
        elif len(current) == len(previous) - 1:

            for j in range(len(previous)):
                if previous[:j]+previous[j+1:] == current:
                    previous = current
                    res[i] = True
                    break

    if all(res):
        return "Family"
    else:
        return "Not a Family"

n = int(input())
for i in range(n):
    a = int(input())
    word = input().split()
    result = belongs_to_family(a, word)
    print(result)

