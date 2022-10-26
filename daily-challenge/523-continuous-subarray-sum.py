from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        ln = len(nums)
        if ln < 2:
            return False

        mapping = {0: -1}
        total = 0
        for idx in range(ln):
            total += nums[idx]
            rem = total % k
            if rem not in mapping:
                mapping[rem] = idx
                continue
            elif idx - mapping[rem] > 1:
                return True
        return False


print(Solution().checkSubarraySum([1, 2, 3, 4, 5], 3))
