#here we are encoding the string
#input: abc
#input: ijk
#here 1 to 8 is a to h similarly 9 to 15 is i to o and 16 to 26 is p to z
#so here we are encoding the string abc to ijk
#output: Yes

def string_encode(st1, st2):


    new_st ="abcdefghijklmnopqrstuvwxyz"
    new_st = list(new_st)

    index_1 = new_st.index(st1[0])
    index_2 = new_st.index(st2[0])

    index = index_2 - index_1

    result = ""

    for i in st1:
        each_index = new_st.index(i)
        final_index = each_index + index
        if final_index > 25:
            actual_index = final_index - 26
            result += new_st[actual_index]
        else:
            result += new_st[final_index]
    if st2 == result:
        print("Yes")
    else:
        print("No")



st1 = input()
st2 = input()
string_encode(st1, st2)
