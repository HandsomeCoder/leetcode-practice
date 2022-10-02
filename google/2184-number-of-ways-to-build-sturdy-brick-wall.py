from collections import defaultdict, deque
from pprint import pprint
from typing import List


class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:

        permutations = []
        def get_permutations(curr):
            nonlocal width, permutations, bricks
            curr_width = curr[-1] if curr else 0
            if curr_width > width:
                return
            if curr_width == width:
                permutations.append(tuple(curr))
                return

            for brick in bricks:
                curr.append(curr_width + brick)
                get_permutations(curr)
                curr.pop()

        get_permutations(deque([]))


        valid_combinations = defaultdict(list)


        for x_perm in permutations:
            x_perm_points = set(x_perm[:-1])

            for y_perm in permutations:
                valid = True
                for y in y_perm:
                    if y in x_perm_points:
                        valid = False
                        break

                if valid:
                    valid_combinations[x_perm].append(y_perm)

        cache = {}
        def dfs(perm, curr_height):
            nonlocal cache
            if curr_height == height: return 1
            
            if prem not in cache:
                cache[prem] = sum(dfs(next_prem, curr_height+1) for next_prem in valid_combinations[prem])

            return cache[prem]


        result, MOD = 0, 1e9+7
        for prem in permutations:
            result += (dfs(prem, 1) % MOD)
        return result

pprint(Solution().buildWall(2, 3, [1, 2]))
