###---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><-
# here we need to convert the given number into roman number
# the input is 1998
# the output should be MCMXCVIII
###---<><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><-



def int_to_roman(num):
    """
    Convert a positive integer to a Roman numeral.
    """

    roman_numeral = ''
    roman_dict = {
        1000: 'M',
        900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
        90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
        9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    for value , symbol in roman_dict.items():
        while num >= value:
            roman_numeral += symbol
            num -= value
    return roman_numeral

n = int(input())
result = int_to_roman(n)
print(result)