from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(l, r, nums):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        ln = len(nums)
        if ln == 1:
            return

        max_value_idx = ln - 1
        min_value_idx = -1
        for i in range(ln-1, -1, -1):
            if nums[i] < nums[max_value_idx]:
                min_value_idx = i
                break

            if nums[max_value_idx] < nums[i]:
                max_value_idx = i

        if min_value_idx == -1:
            reverse(0, ln-1, nums)
            return

        min_value_idx = i
        next_min_value_idx = i+1

        for idx in range(i+1, ln):
            if nums[idx] <= nums[min_value_idx]:
                continue

            if nums[next_min_value_idx] >= nums[idx]:
                next_min_value_idx = idx

        nums[min_value_idx], nums[next_min_value_idx] = nums[next_min_value_idx], nums[min_value_idx]
        reverse(min_value_idx+1, ln-1, nums)


Solution().nextPermutation([2, 3, 1, 3, 3])
Solution().nextPermutation([1, 5, 1])
Solution().nextPermutation([3, 2, 1])
Solution().nextPermutation([1, 3, 2])
Solution().nextPermutation([3, 2, 1])
Solution().nextPermutation([9, 8, 6, 5, 2, 4, 1, 3])
