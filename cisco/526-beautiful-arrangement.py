class Solution:
    arrangement = 0
    cache = {}

    def valid(self, x, y):
        node = (x, y) if x < y else (y, x)
        if node not in self.cache:
            self.cache[node] = (x % y == 0 or y % x == 0)
        return self.cache[node]

    def count(self, start, n, filled):
        if start > n:
            self.arrangement += 1

        for idx in range(n):
            val = idx + 1
            if not filled[idx] and self.valid(val, start):
                filled[idx] = True
                self.count(start+1, n, filled)
                filled[idx] = False

    def countArrangement(self, n: int) -> int:
        self.count(1, n, [False] * n)
        return self.arrangement

