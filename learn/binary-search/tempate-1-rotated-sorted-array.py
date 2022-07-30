from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while(l <= r):
            m = (l+r) // 2
            itr = nums[m]
            if itr == target:
                return m
            elif nums[l] <= itr:
                if nums[l] <= target <= itr:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if itr <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
