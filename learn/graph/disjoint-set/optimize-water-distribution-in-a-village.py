from pprint import pprint
import re
from typing import List


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        roots = [i for i in range(n+1)]
        ranks = [1 for _ in range(n+1)]

        def find(x):
            if roots[x] != x:
                roots[x] = find(roots[x])
            
            return roots[x]

        def unions(x, y):
            xroot = find(x)
            yroot = find(y)

            if xroot != yroot:
                if ranks[xroot] == ranks[yroot]:
                    roots[yroot] = xroot
                    ranks[xroot] += 1
                elif ranks[xroot] > ranks[yroot]:
                    roots[yroot] = xroot
                else:
                     roots[xroot] = yroot

                return True
            
            return False
            
        edges = [(0, i+1, v) for i, v in enumerate(wells)]
        edges.extend(pipes)
        edges.sort(key=lambda x: x[2])

        cost = 0
        n_connected = n+1
        for x, y, c in edges:
            if unions(x, y):
                cost += c
                n_connected -= 1
                if n_connected == 1:
                    break


        return cost





print(Solution().minCostToSupplyWater(5, [1,2,3,2,1], [[1,3,2],[3,5,1],[2,4,1], [5,4,1]]))