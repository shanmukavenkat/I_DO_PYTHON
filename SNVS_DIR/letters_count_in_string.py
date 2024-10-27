text = ''''
My name is S N V S komal i love to have coffe in the morning 
and i love the defender car on of the most hottest car
i have seen in my life and the trust of god and i have done the Zero cloud security
'''
letters = "abcdefghiklmnopqrstuvwxyz"

## text = input('enter the text')

letters_dictionary = {letter:0 for letter in letters }

for char in text.lower():
    if char in letters:
        letters_dictionary[char] +=1
print(letters_dictionary)


