def main():
    string = input("Enter a string: ")
    upper_case = "abcdefghijklmnopqrstuvwxyz"
    is_valid = all(char in upper_case or char == '_' for char in string)

    if is_valid:
        word_count = string.count('_') + 1
        result = f"True {word_count}"
    else:
        result = "False"

    print(result)


main()
