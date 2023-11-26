a = input()
b = input()
#abcd
#abdc

list_1 = list(a)
list_2 = list(b)

length = len(list_1)
for i in range(length):
    if list_1[i] != list_2[i]:
        temp = list_2[i+1]
        list_2[i+1] = list_2[i]
        list_2[i] = temp
        break
if list_1 == list_2:
    print("Yes")
else:
    print("No")
## ~~~SNVSKOMAL
