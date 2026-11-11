"""46. Keep only characters from s that occur in allowed."""


def filter_characters(s, allowed):
    return "".join(c for c in s if c in set(allowed))


print(filter_characters("hello world", "helo"))
