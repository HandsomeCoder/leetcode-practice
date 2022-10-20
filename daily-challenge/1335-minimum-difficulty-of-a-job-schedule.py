from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        cache = {}
        def get_min_with(idx, part, dln):
            nonlocal jobDifficulty, total

            if part == 0:
                return max(jobDifficulty[idx:])

            node = (idx, part)

            if node not in cache:
                max_value, min_value = 0, total

                while dln-(idx+1) >= part:
                    max_value = max(max_value, jobDifficulty[idx])
                    result = get_min_with(idx+1, part-1, dln)
                    min_value = min(min_value, result + max_value)
                    idx += 1

                cache[node] = min_value
            
            return cache[node]

        dln = len(jobDifficulty)

        if dln < d:
            return -1

        total = sum(jobDifficulty)
        if dln == d:
            return total
        elif d == 1:
            return max(jobDifficulty)

        return get_min_with(0, d-1, dln)