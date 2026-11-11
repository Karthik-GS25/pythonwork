"""45. Count and list all ways to climb n steps using 1 or 2."""


def climb(n):
    patterns = []

    def go(left, path):
        if left == 0:
            patterns.append(path)
            return
        if left >= 1:
            go(left - 1, path + [1])
        if left >= 2:
            go(left - 2, path + [2])

    go(n, [])
    return len(patterns), patterns


print(climb(3))
