class Revstring:
    @staticmethod
    def reverse_string(s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

if __name__ == "__main__":
    # Input as a Python list
    k = eval(input("Enter a list of characters (e.g., ['h', 'e', 'l', 'l', 'o']): "))
    result =  Revstring.reverse_string(k)
    print("Reversed List:", result)
