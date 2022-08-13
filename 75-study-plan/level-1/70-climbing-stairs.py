class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        n -= 2
        a, b = 1, 2
        while n:
            a, b = b, a + b
            n -= 1
        
        return b