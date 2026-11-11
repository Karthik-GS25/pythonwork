"""32. Toggle bit k with XOR (k is zero based)."""


def toggle_bit(n, k):
    return n ^ (1 << k)


print(toggle_bit(5, 1))
