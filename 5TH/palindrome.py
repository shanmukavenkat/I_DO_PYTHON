def check_palindrome(string):
    return string == string[::-1]


the_string = input()
print(check_palindrome(the_string))


