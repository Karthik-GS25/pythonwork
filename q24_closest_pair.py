"""24. Find the pair of points with minimum Euclidean distance."""

from math import hypot


def closest_pair(points):
    if len(points) < 2:
        return None
    best = min(
        (
            (hypot(a[0] - b[0], a[1] - b[1]), a, b)
            for i, a in enumerate(points)
            for b in points[i + 1 :]
        ),
        key=lambda item: item[0],
    )
    return best


print(closest_pair([(0, 0), (3, 4), (1, 1)]))
