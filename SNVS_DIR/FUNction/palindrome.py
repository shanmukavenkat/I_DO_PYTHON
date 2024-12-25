def palindrome(n):
    if n[::-1] == n:
        return "It is palindrome"
    else:
        return "It is not palindrome"

n = input()
print(palindrome(n))