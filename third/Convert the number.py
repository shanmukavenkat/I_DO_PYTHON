##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--
#input 9090407368
#----number----divide into three parts----909 040 7368-->convert into alphabets----
#9090407368----9090407368----------------------------->nine zero nine zero four zero seven three six eight
#1111222233---- 1111222233---------------------------->quadruple one triple twotwo double three
##---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><--




def num_to_alpha(num_str):
    alpha = []
    for i in range(len(num_str)):
        if num_str[i] == '0':
            alpha += ['zero']
        elif num_str[i] == '1':
            alpha += ['one']
        elif num_str[i] == '2':
            alpha += ['two']
        elif num_str[i] == '3':
            alpha += ['three']
        elif num_str[i] == '4':
            alpha += ['four']
        elif num_str[i] == '5':
            alpha += ['five']
        elif num_str[i] == '6':
            alpha += ['six']
        elif num_str[i] == '7':
            alpha += ['seven']
        elif num_str[i] == '8':
            alpha += ['eight']
        elif num_str[i] == '9':
            alpha += ['nine']
    return alpha

phone_num = input()
parts = [phone_num[:4], phone_num[4:7], phone_num[7:]]
alpha_parts = [num_to_alpha(p) for p in parts]
output_parts = []


for num in alpha_parts:
    for i in range(len(num)):
        if i > 2 and num[i] == num[i-3] and num[i] == num[i-2] and num[i] == num[i-1]:
            output_parts[-1] = 'quadruple ' +num[i]
        elif i > 1 and num[i] == num[i-2] and num[i] == num[i-1]:
            output_parts[-1] = 'triple ' + num[i]
        elif i > 0 and num[i] == num[i-1]:
            output_parts[-1] = 'double ' + num[i]
        else:
            output_parts.append(num[i])

print(" ".join(output_parts))