"""38. Find maximum container area using two pointers."""


def max_area(height):
    i, j = 0, len(height) - 1
    best = 0
    while i < j:
        best = max(best, (j - i) * min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return best


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
