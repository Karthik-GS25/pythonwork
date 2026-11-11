"""56. Move zeros to the end while preserving non-zero order."""


def move_zeros(values):
    return [x for x in values if x != 0] + [x for x in values if x == 0]


print(move_zeros([0, 1, 0, 3, 12]))
