##here the given sentence which consists of the sentence
#suppouse the sentence is "A game of Letters"
##the output should print like this ==> A ameg of ettersL <==
#here every word should start with the vowel letter

sentence = input().split()

vowels = ["a","e","i","o","u","A","E","I","O","U"]

new_sentence = ""

for word in sentence:

    new_word = ""
    length = len(word)
    for i in range(length):
        if word[i] in vowels:

            new_word = word[i:]+new_word
            break
        else:
            new_word += word[i]


    new_sentence += new_word+" "

print(new_sentence)