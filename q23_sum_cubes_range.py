"""23. Sum cubes from a through b inclusive."""


def sum_cubes(a, b):
    return sum(value**3 for value in range(a, b + 1))


print(sum_cubes(1, 3))
