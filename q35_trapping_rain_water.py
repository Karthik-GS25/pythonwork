"""35. Compute trapped rain water with two pointers."""


def trap(height):
    left, right = 0, len(height) - 1
    lm = rm = water = 0
    while left < right:
        if height[left] <= height[right]:
            lm = max(lm, height[left])
            water += lm - height[left]
            left += 1
        else:
            rm = max(rm, height[right])
            water += rm - height[right]
            right -= 1
    return water


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
