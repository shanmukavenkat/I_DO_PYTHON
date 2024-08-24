"""""
iterate over the string

Get the positions of each character of string 
based on the pattern (1to N and N-1 to 2)

concatenate the characters of a string with 
respect to their positions
 
print the resultants string

P-B-O-N-L-L-R-E-V-G-I-M-O-S
1-2-3-4-3-2-1-2-3-4-3-2-1-2 
"""""


def get_positions(pattern, word_length):
    pattern_length = len(pattern)
    repetitions = word_length // pattern_length  # 10/4 => 2
    extra = word_length % pattern_length  # 10/4 => 2
    positions = pattern * repetitions + pattern[:extra]
    return positions


def get_reordered_word(word, positions, n):
    new_word = ""
    for i in range(1, n + 1):
        for j in range(len(positions)):
            if positions[j] == i:
                new_word += word[j]
    return new_word



def main():
    s = input()
    n = int(input())
    pattern = list(range(1,n+1))+list(range(n-1,1,-1))
    positions = get_positions(pattern,len(s))
    new_word = get_reordered_word(s,positions,n)
    print(new_word)
main()
