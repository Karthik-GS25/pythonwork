"""36. Generate all well-formed n-pair parentheses strings."""


def generate_parentheses(n):
    out = []

    def go(text, open_count, close_count):
        if len(text) == 2 * n:
            out.append(text)
            return
        if open_count < n:
            go(text + "(", open_count + 1, close_count)
        if close_count < open_count:
            go(text + ")", open_count, close_count + 1)

    go("", 0, 0)
    return out


print(generate_parentheses(3))
