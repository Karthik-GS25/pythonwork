"""34. Replace each character in a substring with its predecessor."""


def transform(s, sub):
    i = s.index(sub)
    changed = "".join("z" if c == "a" else chr(ord(c) - 1) for c in sub)
    return s[:i] + changed + s[i + len(sub) :]


print(transform("hackerrank", "hack"))
