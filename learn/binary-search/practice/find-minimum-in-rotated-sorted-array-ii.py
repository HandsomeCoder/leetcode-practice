from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums) - 1

        
        while (l < r):
            m = (l+r) // 2
            itr  = nums[m]
            if itr < nums[r]:
                r = m
            elif itr > nums[r]:
                l = m + 1
            else:
                r -= 1

        return nums[l]