"""1. Find the element that occurs once using XOR."""


def single_number(nums):
    answer = 0
    for value in nums:
        answer ^= value
    return answer


print(single_number([4, 1, 2, 1, 2]))
