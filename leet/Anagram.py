from collections import Counter


def can_re_arrange(s, t):
    return Counter(s) == Counter(t)


"""
    Checks if two strings are anagrams of each other.
    Args:
      s: The first string.
      t: The second string.
    Returns:
      True if the strings are anagrams, False otherwise.
"""


s = input().strip()
t = input().strip()

print(can_re_arrange(s, t))
