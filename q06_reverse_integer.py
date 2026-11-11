"""6. Reverse a signed 32-bit integer with overflow protection."""


def reverse_integer(x):
    sign = -1 if x < 0 else 1
    value = abs(x)
    result = 0
    while value:
        result = result * 10 + value % 10
        value //= 10
    result *= sign
    return result if -(2**31) <= result <= 2**31 - 1 else 0


print(reverse_integer(-123))
