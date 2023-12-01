#Input
#The first line of the input contains an integer T representing the
#number of test cases.
#The next lines of input contain,
#The first line of the input contains an integer N representing the number
#of people living in the village.
#The next N lines of input contains two space-separated strings
#representing the name and nickname of the person.
#Output
#The output should be N lines containing a string. Yes should be
#printed if there is a pair of people with the same name and nickname,
#otherwise No should be printed.
#Explanation
#If the given test cases T  1
#Test case 1 If the given N  3
#Following are the 3 people in the village.
##As person 1 and 3 have the same name and nickname.
#The output should be Yes.
#Sample Input 1
#2
#3
#stephen steve
#sato hanako
#stephen steve
#As person 1 and 3 have the same name and nickname.
#The output should be Yes.

def check_name_nickname(no_of_people_list):
    no_of_people_set = set(no_of_people_list)
    if len(no_of_people_list) == len(no_of_people_set):
        return "No"
    else:
        return "Yes"







def read_names(no_of_people):

    no_of_people_list = []
    for i in range(no_of_people):
        name_nickname = input()
        no_of_people_list.append(name_nickname)
    return no_of_people_list








no_of_test_cases = int(input())

for i in range(no_of_test_cases):
    no_of_people = int(input())
    no_of_people_list = read_names(no_of_people)
    final_result = check_name_nickname(no_of_people_list)
    print(final_result)