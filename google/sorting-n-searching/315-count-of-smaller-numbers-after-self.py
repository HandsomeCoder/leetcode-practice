from bisect import insort
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        def search(sorted_nums, x, low, high):
            l, r = low, high
            while l < r:
                m = (l + r) // 2
                if sorted_nums[m] >= x:
                    r = m
                else:
                    l = m + 1

            while r >= low and sorted_nums[r] == x:
                r -= 1

            return r if sorted_nums[r] >= x else r + 1

        def sort(nums, l, r):
            while l < r and nums[l] > nums[l+1]:
                nums[l], nums[l+1] = nums[l+1], nums[l]
                l += 1

        ln = len(nums)
        if ln == 1:
            return [0]

        result = [-1 for _ in range(ln)]
        idx = ln-2
        result[-1] = 0
        while idx > -1:
            num = nums[idx]
            sidx = search(nums, num, idx+1, ln-1)
            result[idx] = 0 if sidx == idx else sidx - idx - 1
            sort(nums, idx, ln-1)
            idx -= 1
        return result

print(Solution().countSmaller([26, 78, 27, 100, 33, 67, 90, 23, 66, 5, 38, 7, 35, 23, 52, 22,
      83, 51, 98, 69, 81, 32, 78, 28, 94, 13, 2, 97, 3, 76, 99, 51, 9, 21, 84, 66, 65, 36, 100, 41]))
