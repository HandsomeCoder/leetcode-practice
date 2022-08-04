from bisect import bisect_left
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ln = len(arr)

        if(ln == k):
            return arr

        ln -= 1
        l, r = 0, ln

        while(l+1 < r):
            m = (l+r) // 2
            itr = arr[m]
            if itr == x:
                break
            elif itr > x:
                r = m
            else:
                l = m

        p = l if abs(arr[l] - x) <= abs(arr[l+1] - x) else l+1
        if k == 1:
            return [arr[p]]
        elif p == 0:
            return arr[:k]
        elif p == ln:
            return arr[-k:]

        l, r = p, p
        k -= 1
        while(k > 0):
            next_l = l - 1
            if next_l < 0:
                r += k
                break

            next_r = r + 1
            if next_r > ln:
                l -= k
                break

            if abs(arr[next_l] - x) <= abs(arr[next_r] - x):
                l = next_l
            else:
                r = next_r
            k -= 1

        return arr[l:r+1]


print(Solution().findClosestElements([0, 1, 1, 1, 2, 3, 6, 7, 8, 9], 9, 4))
print(Solution().findClosestElements([1, 3], 1, 2))
print(Solution().findClosestElements([1, 10, 15, 25, 35, 45, 50, 59], 1, 30))
print(Solution().findClosestElements([1, 2, 3, 4, 4, 4, 4, 5, 5], 3, 3))
print(Solution().findClosestElements([1, 1, 2, 2, 3, 3, 6, 7, 8, 9, 9, 11, 11, 12, 12, 12, 13, 15, 18, 18, 21,
 22, 22, 23, 25, 25, 32, 33, 34, 37, 37, 38, 38, 39, 39, 40, 41, 43, 43, 45, 45, 46, 46, 48, 48, 49, 50, 50, 53,
  53, 54, 54, 56, 57, 57, 58, 58, 60, 60, 61, 62, 63, 63, 66, 69, 70, 71, 71, 71, 74, 75, 75, 76, 76, 80, 81, 81, 
  82, 84, 86, 86, 87, 87, 87, 88, 90, 91, 93, 93, 93, 94, 94, 94, 95, 96, 97, 98, 98, 98, 99], 3,
                                     13))
