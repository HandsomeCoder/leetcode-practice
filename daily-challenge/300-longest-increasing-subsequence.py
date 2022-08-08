from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []

        for num in nums:
            match_idx = bisect_left(stack, num)

            if len(stack) == match_idx:
                stack.append(num)
            else:
                stack[match_idx] = num   

        return len(stack)
