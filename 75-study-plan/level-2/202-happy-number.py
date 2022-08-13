class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)

        visited = set([])
        cache = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        while True:
            next = 0
            for ch in n:
                num = int(ch)
                next += cache[num]

            if next == 1:
                return True

            if next in visited:
                return False

            visited.add(next)
            n = str(next)
