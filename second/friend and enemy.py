#Test Case: If the given numbers 3 1 5 2 1,
#In the range from 1 to 5, the number 1 has occurred twice
#and the number 4 is missing.
#So, 1 is the enemy's shirt number, and 4 is the person's shirt
#number who was kidnapped.
#The output should be 1 4.

friends_list = list(map(int,input().split()))


F = len(friends_list)

result = ""
for i in range(1,F+1):
    count = friends_list.count(i)
    if count >= 2:
        result += str(i) + " "

for i in range(1,F+1):

    if i not in friends_list:

        result += str(i)


print(result)