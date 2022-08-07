from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        def helper(m):
            x, count = 0
            for y, val in enumerate(nums):
                while val - nums[x] > m:
                    x += 1
                count += y - x

                if count >= k:
                    return True
            return False


        nums.sort()
        l, r  = 0, nums[-1] - nums[0]

        while(l < r):
            m = (l + r) // 2

            if helper(m):
                r = m
            else:
                l = m + 1

        return l