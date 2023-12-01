#input given 2
#{noon moon}the second player's word cannot be formed by
#{part trap} rearranging the letters of the first player's word.
#the output should be printed as NO YES
#considering the first input as noon and second input as moon

def SwapCompetition(word):
    wordone = word[0]
    wordtwo = word[1]
    wordone_op = sorted(wordone)
    wordtwo_op = sorted(wordtwo)
    if wordone_op == wordtwo_op:
        return "YES"
    else:
        return "NO"

n = int(input())
output = ""
for i in range(n):
    word = input().lower()
    word = word.split()
    output_fun = SwapCompetition(word)
    output += output_fun + " "
print(output)