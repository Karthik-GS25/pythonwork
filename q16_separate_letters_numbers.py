"""16. Extract letters and digits in their original order."""


def separate(s):
    return ["".join(c for c in s if c.isalpha()), "".join(c for c in s if c.isdigit())]


print(separate("a1b2c3"))
