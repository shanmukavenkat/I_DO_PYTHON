##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#here the input is given like AAA
#and the output should be like 703
#Peter is making a new dictionary. He wants to arrange the words in
#the ascending order of their length and later arrange the ones with
#the same length in lexicographic order. Each word is given a serial
#number according to its position. Find the word according to the
#serial number
##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--


def num_to_alpha(num):
    alpha = ''
    while num >0:
        num -= 1
        alpha = chr(num % 26 + 65) + alpha
        num //= 26
    return alpha

num = int(input())
alpha = num_to_alpha(num)
print(alpha)