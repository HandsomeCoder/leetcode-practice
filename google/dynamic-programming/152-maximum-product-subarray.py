
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln == 1:
            return nums[0]

        max_sum = pos_sum = neg_sum = nums[0]

        for num in nums[1:]:
            lps, nps = pos_sum * num, neg_sum * num
            pos_sum, neg_sum = max(num, lps, nps), min(num, lps, nps)

            max_sum = max(max_sum, pos_sum)
        return max_sum

        ln = len(nums)
        if ln == 1:
            return nums[0]

        pos_sum = neg_sum = 0
        max_sum = -inf
        for num in nums:
            if num == 0:
                max_sum = max(max_sum, num, pos_sum, neg_sum)
                pos_sum = neg_sum = 0
                continue

            if num > 0:
                pos_sum = max(num, pos_sum * num)
                neg_sum = min(num, neg_sum * num)
            else:
                pos_sum, neg_sum = max(
                    num, neg_sum * num), min(num, pos_sum * num)

            max_sum = max(max_sum, num, pos_sum, neg_sum)

        return max(max_sum, pos_sum, neg_sum)  


print(Solution().maxProduct([6, -2, 3, -4, 0, 5, -7, 2]))
print(Solution().maxProduct([-1, -1]))
print(Solution().maxProduct([-1, 0, -2]))
print(Solution().maxProduct([-2, 3, -4]))
