from collections import deque
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ln = len(graph)
        src, target = 0, ln - 1 
        visited = [False] * ln

        stack = deque([(src, tuple())])

        result = []
        while stack:
            node, path = stack.pop()
            
            if node == target:
                path = list(path)
                path.append(node)
                result.append(path)
                for p in path[1:]:
                    visited[p] = False

            if visited[node]:
                continue

            visited[node] = True
            for neigh in graph[node]:
                stack.append((neigh, path + (node,)))

        return result


print(Solution().allPathsSourceTarget([[2],[],[1]]))