"""28. Check whether two strings are anagrams."""

from collections import Counter


def is_anagram(s, t):
    return Counter(s) == Counter(t)


print(is_anagram("anagram", "nagaram"))
