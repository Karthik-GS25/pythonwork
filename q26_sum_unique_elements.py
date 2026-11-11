"""26. Sum values that occur exactly once."""

from collections import Counter


def sum_unique(nums):
    counts = Counter(nums)
    return sum(value for value, count in counts.items() if count == 1)


print(sum_unique([1, 2, 3, 2]))
