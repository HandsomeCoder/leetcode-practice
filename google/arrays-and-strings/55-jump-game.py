from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ln = len(nums)
        left = ln - 2

        last_index = ln - 1
        while left >= 0:
            if left + nums[left] >= last_index:
                last_index = left

            left -= 1

        return last_index == 0
