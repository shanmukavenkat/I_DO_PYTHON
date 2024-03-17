"Each character in the string should either be a uppercase letter and underscore"

Upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def is_uppercase_letter(letter):
    return letter in Upper_case


def is_underscore(character):
    return character == '_'


def all_statisfied(results):
    final_result = True
    for result in results:
        final_result = final_result and result
    return final_result


def get_no_of_words(string):
    return len(string.split('_'))


def is_valid_string(string):
    results = []
    for character in string:
        result = is_uppercase_letter(character) or is_underscore(character)
        results.append(results)
    return all_statisfied(results)


def main():
    string = input()
    is_valid = is_valid_string(string)
    if is_valid:
        result = "True " + str(get_no_of_words(string))
    else:
        result = "False"
    print(result)


main()



