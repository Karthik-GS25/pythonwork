"""15. Reverse all 32 bits of an integer."""


def reverse_bits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result


print(reverse_bits(43261596))
