#Anil has been given a word W and N number of sentences.
# He needs to find the sentence number in which the word W appears for the first time in the N sentences.
# Help Anil find the sentence number by writing a program that reads the word W and the N number of sentences and
# prints the sentence number in which the word W appears for the first time in N sentences.

#Approach


#Read the N sentences and store them in a list.
#Iterate through the list of sentences and check if the word W is present in each sentence.
#If the word W is found in a sentence, print the sentence number and stop the search.
#If the word W is not found in any sentence, print -1

#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#Step-by-Step Explanation
#Step 1: Read the word and number of sentences
#Read the input word W using the input() function.
#Read the number of sentences N using the input() function
# and convert it to an integer using the int() function.
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#Step 2: Read the sentences
#Create a function read_sentences(n) that takes the number of sentences n as an argument.
#Inside the function, create an empty list called sentences_list.
#Use a for loop to iterate n times.
#For each iteration, read a sentence using the input() function,
# split it into words using the split() function, and append the list of words to sentences_list.
#Return the sentences_list after the loop.
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--


#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#Step 3: Find the sentence containing the word
#Create a function
# find_the_sentence_contains_the_word(sentences_list, word) that takes the sentences_list and the word W as arguments.
#Inside the function, use a for loop to iterate through the sentences_list.
#For each sentence, check if the word W is present in the sentence using the in keyword.
#If the word W is found in a sentence,
# calculate the sentence position by adding 1 to the index and return the sentence position.
##If the word W is not found in any sentence, return -1.
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#Step 4: Print the sentence number
#In the main() function, call the read_sentences(no_of_sentences) function to get the sentences_list.
#Call the find_the_sentence_contains_the_word(sentences_list, word) function to get the sentence_position.
#Print the sentence_position.
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--

def read_sentences(n):
    sentences_list = []
    for i in range(n):
        sentence = input().split()
        sentences_list.append(sentence)
    return sentences_list


def find_the_sentence_contains_the_word(sentences_list, word):
    for index in range(len(sentences_list)):
        if word in sentences_list[index]:
            sentence_postion = index + 1
            return sentence_postion
    return -1


def main():
    word = input()
    no_of_sentences = int(input())
    sentences_list = read_sentences(no_of_sentences)
    sentence_postion = find_the_sentence_contains_the_word(sentences_list, word)
    print(sentence_postion)


main()

#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--


#a = input()
#b = int(input())
#empty_list = []

#for i in range(b):
#    empty_list.append(list(map(str, input().split())))

#l = []
#for each in empty_list:
#    if a in each:
#       print(empty_list.index(each)+1)
#        break
#    else:
#        l.append(0)

#if len(l)==b:
#    print("-1")
#---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
