from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while(l < r):
            m = (l+r) // 2
            itr = nums[m]
            rn = nums[m+1]
            if itr > rn:
                r = m
            elif itr < rn:
                l = m + 1
            else:
                return l
                
        return l
