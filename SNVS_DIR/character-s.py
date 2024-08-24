def isValid(s):
    stack = []
    matching_bracket = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in matching_bracket:
            if not stack or stack[-1] != matching_bracket[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0

s = input("Enter the string of parentheses: ")
k = isValid(s)
print(k)
