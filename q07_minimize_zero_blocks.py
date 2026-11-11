"""7. Generate all strings with K ones and find minimum zero block."""


def arrangements(L, K):
    result = []

    def make(prefix, ones):
        if len(prefix) == L:
            zeros = prefix.split("1")
            result.append((prefix, max(map(len, zeros))))
            return
        if ones < K:
            make(prefix + "1", ones + 1)
        if len(prefix) - ones < L - K:
            make(prefix + "0", ones)

    make("", 0)
    best = min(v for _, v in result)
    return result, [s for s, v in result if v == best], best


print(arrangements(4, 2))
