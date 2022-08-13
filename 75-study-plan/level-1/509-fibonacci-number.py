from math import sqrt


class Solution:
    def fib(self, n: int) -> int:
        sqrt5 = sqrt(5)
        goldenRatio = (1 + sqrt5) / 2
        return int(round(pow(goldenRatio, n) / sqrt5 ))