"""22. Compute the midpoint of two points."""


def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


print(midpoint((0, 0), (4, 4)))
