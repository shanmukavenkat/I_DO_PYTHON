#If the given A =mari , B=to , C =zzo and T=1321
#Concatenate these in the order A  C  B  A based on the order of
#digits in the given number T .
#So the resultant string is marizzotomari .
#The output should be marizzotomari
#1 = mari 2 = to 3 = zzo

new_dictionary = {}
for i in range(1,4):
    new_dictionary[str(i)] = input()

result = ""
number = input()
for j in number:
    result += new_dictionary[j]
print(result)