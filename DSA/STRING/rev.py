from typing import List


def reverseString(self, s: List[str]) -> list[str]:
    return list(s[::-1])

k = input()
s = k
print(reverseString(k,s))