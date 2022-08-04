from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ln = len(arr)-1
        l, r = 0, ln

        p = 0 
        min_v = arr[-1]
        while(l < r):
            m = (l+r) // 2
            itr = abs(arr[m] - k)
            if itr == 0:
                p = m
                break
            elif itr < min_v: 
                min_v = itr
                if arr[m] < k:
                    l = m + 1
                else:
                    r = m - 1
            

        if k == 1:
            return [arr[p]]
        elif p == 0:
            return arr[:k]
        elif p == ln:
            return arr[-k:]

        s = k // 2
        a = p - s
        b = p + s
        if k | 1 > k:
            b -= 1
           
        return arr[a: b+1]
        

print(Solution().findClosestElements([1],1,1))