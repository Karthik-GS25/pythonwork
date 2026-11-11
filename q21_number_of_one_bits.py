"""21. Count set bits in a positive integer."""


def hamming_weight(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


print(hamming_weight(11))
