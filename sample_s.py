nu = "6.351"
print(round(float(nu),0))
a = "2.456"
b = "3.456"
is_greater = (round(float(a)) > round(float(b)))
print(len(a))
print((a > b) == is_greater)
print("---------------------------^^^^^^^^^^^^^^_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
cah = "1"
p = ord(cah)
re = p/3
print(round(re,2))
print("---------------------------")
bill = 32.26
print(type(round(bill,1)))
print("---------------------------")
op = 1+9/1+2
print(round(op) != 4)
print("---------------------------")
print(round(8.546))
print("---------------------------")
wor = "4.652"
new_str = wor*2
new_str = new_str[4:]
new_str = float(new_str.strip("."))
print(round(new_str))
print("---------------------------")
num = "23.56"
if (num.isdigit()):
    num = round(num,1)
else:
    num = round(float(num),1)
print(num)
print("---------------------------")
numb = 3.461
print(int(numb) == round(numb))
print("---------------------------")
#value = "2.561"
#val = int(value)
#print(round(val),0)
print("---------------------------")
total = round((6.5+0.50),1)
is_equal = (total == 7.1)

print(is_equal)
print(is_equal == "True")
print("---------------------------")
float_n = 4.6578
for i in range(1,3):
    print(round(float_n,i))

print("---------------------------")
