from collections import deque
from turtle import st


class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if x == 0: return 0
        if n == 0: return 1

        negative = n < 0
        n = abs(n)

        i = n
        res = 1
        itr = x
        while i > 0:
            if i & 1:
                res = res * itr
            itr = itr * itr 
            
            i = i // 2

        return round(1/res if negative else res, 5)