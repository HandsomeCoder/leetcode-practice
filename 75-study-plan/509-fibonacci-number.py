class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1

        a, b = 0, 1
        n -= 1
        while n:
            a, b = b, a + b
            n -= 1
        return b

print(Solution().fib())