from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        ln = len(nums)
        for idx in range(ln):
            num = nums[idx]
            if num in seen and abs(seen[num] - idx) <= k:
                return True

            seen[num] = idx
