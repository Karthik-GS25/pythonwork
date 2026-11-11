"""14. Merge k sorted linked lists (lists may be Python iterables)."""

import heapq


def merge_k_sorted_lists(lists):
    return list(heapq.merge(*lists))


print(merge_k_sorted_lists([[1, 4], [1, 3], [2]]))
