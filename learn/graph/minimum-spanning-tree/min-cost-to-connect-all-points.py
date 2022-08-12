from collections import defaultdict
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ln = len(points)
        edges = []
        for i in range(ln):
            x, y = points[i]
            key = (x, y)
            for j in range(i+1, ln):
                a, b = points[j]
                neigh = (a, b)
                cost = abs(x-a) + abs(y-b)
                edges.append((cost, key, neigh))

        edges.sort(key=lambda x: x[0])


        ranks = {tuple(node): 1 for node in points}
        roots = {tuple(node): tuple(node) for node in points}


        def find(src):
            if src != roots[src]:
                roots[src] = find(roots[src])
        
            return roots[src]

        def union(src, dest):
            rsrc = find(src)
            rdest = find(dest)

            if rsrc != rdest:
                if ranks[rsrc] == ranks[rdest]:
                   roots[rdest] = rsrc
                   ranks[rsrc] += 1
                elif ranks[rsrc] > ranks[rdest]: 
                    roots[rdest] = rsrc
                else:
                   roots[rsrc] = rdest 
                
                return True

            return False 


        connection = ln - 1
        total_cost = 0
        for cost, p1, p2 in edges:
            if union(p1, p2):
                connection -= 1
                total_cost += cost
                if connection == 0:
                    break

        return total_cost
            
        
print(Solution().minCostConnectPoints([[7,18],[-15,19],[-18,-15],[-7,14],[4,1],[-6,3]]))