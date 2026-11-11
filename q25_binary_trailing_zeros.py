"""25. Count trailing zeros in a binary representation."""


def trailing_zeros(n):
    if n == 0:
        return 0
    count = 0
    while n & 1 == 0:
        count += 1
        n >>= 1
    return count


print(trailing_zeros(40))
