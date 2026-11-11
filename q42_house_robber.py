"""42. Maximum money without robbing adjacent houses."""


def rob(nums):
    previous = best = 0
    for money in nums:
        previous, best = best, max(best, previous + money)
    return best


print(rob([2, 7, 9, 3, 1]))
