from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = prev_max = -100000
        for num in nums:
            prev_max = max(num, num + prev_max)
            max_sum = max(max_sum, prev_max)

        return max_sum