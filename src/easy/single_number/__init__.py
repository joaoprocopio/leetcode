# https://leetcode.com/problems/single-number/


def single_number(nums: list[int]) -> int:
    for num in nums:
        count: int = nums.count(num)
        if count == 1:
            return num

    return -1
