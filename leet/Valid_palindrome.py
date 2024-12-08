import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove unwanted characters and convert to lowercase
        cleaned_string = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

        # Check if the cleaned string is the same as its reverse
        return cleaned_string == cleaned_string[::-1]
