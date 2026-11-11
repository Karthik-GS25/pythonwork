"""11. Find the missing number from 0 through n."""


def missing_number(nums):
    return len(nums) * (len(nums) + 1) // 2 - sum(nums)


print(missing_number([3, 0, 1]))
