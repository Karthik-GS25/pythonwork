"""3. Regular expression matching for . and *."""


def is_match(s, p):
    memo = {}

    def match(i, j):
        if (i, j) in memo:
            return memo[i, j]
        if j == len(p):
            result = i == len(s)
        else:
            first = i < len(s) and (p[j] == s[i] or p[j] == ".")
            result = (
                (match(i, j + 2) or (first and match(i + 1, j)))
                if j + 1 < len(p) and p[j + 1] == "*"
                else first and match(i + 1, j + 1)
            )
        memo[i, j] = result
        return result

    return match(0, 0)


print(is_match("abcd", ".*"))
