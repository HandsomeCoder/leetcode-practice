from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1

        while l + 1 < r:
            m = (l+r) // 2

            if arr[m-1] < arr[m] > arr[m+1]:
                return m
            elif arr[m-1] > arr[m] > arr[m+1]:
                r = m
            else:
                l = m

        return l + 1


print(Solution().peakIndexInMountainArray(
    [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))
