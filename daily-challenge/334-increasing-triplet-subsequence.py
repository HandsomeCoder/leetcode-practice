from bisect import bisect_left
from collections import deque
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ln = len(nums)
        if ln < 3:
            return False

        stack = deque([nums[0]])

        for idx in range(1, ln):
            num = nums[idx]
            if stack[-1] < num:
                stack.append(num)
            elif stack[-1] > num:
                idx = bisect_left(stack, num)
                stack[idx] = num

            if len(stack) == 3:
                return True

        return False


print(Solution().increasingTriplet([2, 1, 5, 0, 7, 4, 6]))
