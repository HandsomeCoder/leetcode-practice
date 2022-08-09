from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        visited = [False for _ in range(n)]
        province = 0
        for i in range(n):
            if not visited[i]:
                province += 1
                queue = deque([i])

                while queue:
                    node = queue.popleft()
                    if visited[node]:
                        continue

                    visited[node] = True
                    for j in range(n):
                        if (isConnected[node][j] == 1) and (not visited[node]) :
                            queue.append(j)

        return province
        # n = len(isConnected)
        # if n == 1:
        #     return 1

        # root = [i for i in range(n)]
        # rank = [1 for _ in range(n)]

        # def find(i):
        #     if i == root[i]:
        #         return i
            
        #     root[i] = find(root[i])
        #     return root[i]

        # def union(i, j):
        #     ri = find(i)
        #     rj = find(j)

        #     if ri != rj:
        #         if rank[ri] == rank[rj]:
        #             root[rj] = ri
        #             rank[ri] += 1 
        #         elif rank[ri] > rank[rj]:
        #             root[rj] = ri
        #         else:
        #             root[ri] = rj        
            

        # for i in range(n):
        #     for j in range(i, n):
        #         if i != j and isConnected[i][j] == 1:
        #             union(i, j)

        # province = set()
        # for i in range(n):
        #     province.add(find(i))

        # return len(province)

print(Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))