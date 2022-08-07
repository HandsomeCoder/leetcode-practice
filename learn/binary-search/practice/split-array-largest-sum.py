from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        if m == 1:
            return sum(nums)

        l, r = max(nums), sum(nums)

        res = r
        while l <= r:
            max_value = (l + r) // 2
        
            curr_sum = split_requires = 0
            for num in nums:
                if curr_sum + num > max_value:
                    split_requires += 1
                    curr_sum = num
                else:
                    curr_sum += num

            split_requires += 1
        
            if split_requires > m:
                l = max_value + 1
            else:
                r = max_value - 1
                res = max_value
                
        return res