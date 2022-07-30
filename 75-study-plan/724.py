from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = 0
        total = 0
        for itr in nums:
            total += itr
            n += 1
        
        ls = 0
        idx = 0
        while(idx < n):
            itr = nums[idx]
            if(ls == total - ls - itr):
                return idx

            ls += itr
            idx += 1

        return -1
