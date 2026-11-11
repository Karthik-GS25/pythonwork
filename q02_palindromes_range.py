"""2. List palindromes in an inclusive range."""


def palindromes_in_range(m, n):
    return [value for value in range(m, n + 1) if str(value) == str(value)[::-1]]


print(palindromes_in_range(10, 50))
