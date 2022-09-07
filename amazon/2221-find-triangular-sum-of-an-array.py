from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
  
        def mod_10(x):
            return x - 10 if x >= 10 else x
  
        ln = len(nums) - 1

        while ln:
            for idx in range(ln):
                nums[idx] = mod_10(nums[idx] + nums[idx+1])

            ln -= 1

        return nums[0]


print(Solution().triangularSum([1, 2, 3, 4, 5]))
