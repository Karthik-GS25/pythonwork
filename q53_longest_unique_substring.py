"""53. Sliding-window length of longest substring without repeats."""


def longest_unique(s):
    present = [False] * 26
    left = best = 0
    for right, ch in enumerate(s):
        index = ord(ch.lower()) - 97
        while present[index]:
            present[ord(s[left].lower()) - 97] = False
            left += 1
        present[index] = True
        best = max(best, right - left + 1)
    return best


print(longest_unique("abcabcbb"))
