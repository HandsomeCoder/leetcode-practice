from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        ln = len(nums)

        if ln <= 2:
            return max(nums)

        max_val, curr = nums[0], nums[1]

        for idx in range(2, ln):
            num = nums[idx]
            temp = num + max_val
            max_val = max(curr, max_val)
            curr = temp

        return max(max_val, curr)


print(Solution().rob([4, 2, 3, 9]))
print(Solution().rob([4, 2, 3, 1]))
print(Solution().rob([1, 2, 3, 1]))
print(Solution().rob([2, 7, 9, 3, 1]))
