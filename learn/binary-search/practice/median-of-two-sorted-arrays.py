from math import inf
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        total = l1 + l2
        n, m = l1-1, l2-1

        def get1(idx):
            return nums1[idx] if idx < l1 else nums2[idx - l1]

        def get2(idx):
            return nums2[idx] if idx < l2 else nums1[idx - l2]

        med = total // 2
        if l1 == 0:
            if total & 1:
                return nums2[med]
            else:
                return (nums2[med] + nums2[med-1]) / 2.0
        elif l2 == 0:
            if total & 1:
                return nums1[med]
            else:
                return (nums1[med] + nums1[med-1]) / 2.0
        elif nums1[n] < nums2[0]:
            if total & 1:
                return get1(med)
            else:
                return (get1(med) + get1(med-1)) / 2.0
        elif nums1[0] > nums2[m]:
            if total & 1:
                return get2(med)
            else:
                return (get2(med) + get2(med-1)) / 2.0
        else:
            X, Y, Xlen, Ylen = nums1, nums2, l1, l2
            if l1 > l2:
                X, Y, Xlen, Ylen = Y, X, l2, l1

            l, r = 0, Xlen - 1
            MIN_V, MAX_V = min(X[0], Y[0])-1, max(X[Xlen-1], Y[Ylen-1])+1
            while True:
                m1 = (l + r) // 2
                m2 = med - m1 - 2

                Xl = X[m1] if m1 >= 0 else MIN_V
                Xr = X[m1+1] if m1+1 < Xlen else MAX_V
                Yl = Y[m2] if m2 >= 0 else MIN_V
                Yr = Y[m2+1] if m2+1 < Ylen else MAX_V

                if(Xl <= Yr and Yl <= Xr):
                    if total & 1:
                        return min(Xr, Yr)
                    else:
                        return (max(Xl, Yl) + min(Xr, Yr)) / 2.0
                elif Xl > Yr:
                    r = m1 - 1
                else:
                    l = m1 + 1


print(Solution().findMedianSortedArrays([1, 3], [2]))
print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
print(Solution().findMedianSortedArrays([100001], [100000]))
print(Solution().findMedianSortedArrays(
    [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5]))
print(Solution().findMedianSortedArrays(
    [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4]))
print(Solution().findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
