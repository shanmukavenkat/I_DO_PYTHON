#here user will give the input as 2
#here if the number is odd it should be 1 and the bulb on
#here if the number is even it should be 0 and the bulb off
#here the output should be 1 0
#here the output should be 0 1

num = int(input())

intiL_bulb = []
for i in range(num):

    if i%2 ==0:
        intiL_bulb.append(1)
    else:
        intiL_bulb.append(0)
print(*intiL_bulb)

for i in range(1,num):

    new_bulb = []
    for each_bulb in intiL_bulb:
        if each_bulb == 1:
            new_bulb.append(0)
        else:
            new_bulb.append(1)
    intiL_bulb = new_bulb
    print(*intiL_bulb)