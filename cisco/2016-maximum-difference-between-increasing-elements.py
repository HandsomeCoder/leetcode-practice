from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_value, max_diff = nums[0], -1

        for idx in range(1, len(nums)):
            num = nums[idx]
            if min_value > num:
                min_value = num
            
            max_diff = max(max_diff, num - min_value)

        return -1 if max_diff == 0 else max_diff
