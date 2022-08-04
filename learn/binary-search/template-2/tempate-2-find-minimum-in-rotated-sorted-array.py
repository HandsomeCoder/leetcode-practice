from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if nums[0] < nums[-1]:
            return nums[0]

        l, r = 0, len(nums) - 1
        
        if r == 1:
            return min(nums)

        while(l < r):
            m = (l + r) // 2
            itr = nums[m]
            rend = nums[r]

            if itr < rend:
                r = m
            else:
                l = m + 1

        return nums[l]
