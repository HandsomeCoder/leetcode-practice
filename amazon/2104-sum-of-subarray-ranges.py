from collections import deque
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ln = len(nums)
        result = [0 for _ in range(ln+1)]

        stack = deque([])
        prev_min = [-1 for _ in range(ln)]
        for idx in range(ln):
            num = nums[idx]
            while stack and nums[stack[-1]] > num:
                stack.pop()
            if stack:
                prev_min[idx] = stack[-1]
            stack.append(idx)

        for idx in range(ln):
            result[idx] = result[prev_min[idx]] + ((idx - prev_min[idx]) * nums[idx])

        min_sum = sum(result)
        stack = deque([])
        prev_max = [-1 for _ in range(ln)]
        for idx in range(ln):
            num = nums[idx]
            while stack and nums[stack[-1]] < num:
                stack.pop()
            if stack:
                prev_max[idx] = stack[-1]
            stack.append(idx)

        for idx in range(ln):
            result[idx] = result[prev_max[idx]] + ((idx - prev_max[idx]) * nums[idx])

        return sum(result) - min_sum

print(Solution().subArrayRanges([4, -2, -3, 4, 1]))
