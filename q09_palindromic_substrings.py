"""9. Count palindromic substrings, retaining duplicate positions."""


def palindromic_substrings(s):
    result = []
    for center in range(2 * len(s) - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < len(s) and s[left] == s[right]:
            result.append(s[left : right + 1])
            left -= 1
            right += 1
    return result


print(palindromic_substrings("ababa"))
