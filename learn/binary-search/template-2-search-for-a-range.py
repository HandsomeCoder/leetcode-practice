from math import ceil
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ln = len(nums) - 1

        if ln == -1:
            return [-1, -1]

        l1, r1, l2, r2 = 0, ln, 0, ln
        while(l1 < r1 or l2 < r2):
            m1 = (l1+r1) // 2
            m2 = ceil((l2+r2) / 2)

            if nums[m1] == target:
                r1 = m1
            elif nums[m1] > target:
                r1 = m1 - 1
            else:
                l1 = m1 + 1

            if nums[m2] == target:
                l2 = m2
            elif nums[m2] > target:
                r2 = m2 - 1
            else:
                l2 = m2 + 1

        if nums[l1] == target and nums[r2] == target:
            return [l1, r2]
        else:
            return [-1, -1]




print(Solution().searchRange([5], 5))
print(Solution().searchRange([5,5], 5))
print(Solution().searchRange([5,5,5], 5))
print(Solution().searchRange([5,5,5,5], 5))
print(Solution().searchRange([1,2,3,4,5,5,5,5,6,7,8,9], 5))
print(Solution().searchRange([5,7,7,8,8,10], 8))

