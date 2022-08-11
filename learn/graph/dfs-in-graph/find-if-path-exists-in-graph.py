from collections import defaultdict, deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        neighbours = defaultdict(list)

        for x, y in edges:
            neighbours[x].append(y)
            neighbours[y].append(x)

        stack = deque([source])
        visited = [False] * n
        while stack:
            node = stack.pop()

            if visited[node]:
                continue
                
            if node == destination:
                return True

            visited[node] = True

            stack.extend(neighbours[node])

        return False