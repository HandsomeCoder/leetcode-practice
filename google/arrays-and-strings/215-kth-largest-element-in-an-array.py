import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            swap_idx = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[swap_idx] = nums[swap_idx], nums[i] 
                    swap_idx += 1

            nums[swap_idx], nums[right] = nums[right], nums[swap_idx]

            return swap_idx

        def select(left, right, k_large_elements):

            pivot_idx = partition(left, right, (left + right) // 2)

            if k_large_elements == pivot_idx:
                return nums[pivot_idx]
            elif k_large_elements > pivot_idx:
                return select(pivot_idx + 1, right, k_large_elements)
            else:
                return select(left, pivot_idx - 1, k_large_elements)

        if len(nums) == 1:
            return nums[0]
        elif k == 1:
            return max(nums)

        return select(0, len(nums)-1, len(nums) - k)


print(Solution().findKthLargest(
    [3, 2, 3, 1, 2, 4, 5, 5, 6],
    4))
