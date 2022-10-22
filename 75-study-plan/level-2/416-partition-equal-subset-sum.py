from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def find(idx, curr, target):
            nonlocal nums, ln, cache

            if target == curr:
                return True

            if idx == ln or target < curr:
                return False

            node = (idx, curr)
            if node not in cache:
                with_num = find(idx + 1, curr + nums[idx], target)
                if with_num:
                    return True

                without = find(idx + 1, curr, target)
                cache[node] = with_num or without

            return cache[node]

        total = sum(nums)

        if total & 1 == 1:
            return False

        ln = len(nums)
        cache = {}
        return find(0, 0, total // 2)