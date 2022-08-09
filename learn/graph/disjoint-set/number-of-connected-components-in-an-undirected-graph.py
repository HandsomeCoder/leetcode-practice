from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        roots = [i for i in range(n)]
        ranks = [1 for _ in range(n)]
        ngraph = n

        def find(x):
            if roots[x] != x:
                roots[x] = find(roots[x])
            
            return roots[x]

        def union(x, y):
            xr = find(x)
            yr = find(y)

            if xr != yr:
                if ranks[xr] == ranks[yr]:
                    roots[yr] = xr
                    ranks[xr] += 1
                elif ranks[xr] > ranks[yr]:
                    roots[yr] = xr
                else:
                    roots[xr] = yr

                return True
            
            return False

        for i, j in edges:
            if union(i, j):
                ngraph -= 1

        return ngraph