from typing import List

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        logs.sort(key=lambda x: x[0])
        
        roots = [i for i in range(n)]
        ranks = [1 for _ in range(n)]

        def find(x):
            if x != roots[x]:
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
                    roots[xr] = yr
                else:
                    roots[yr] = xr

                return True

            return False

        connected_nodes = n
        for t, i, j in logs:        
            if union(i, j):
                connected_nodes -= 1
                if connected_nodes == 1:
                    return t

        return -1