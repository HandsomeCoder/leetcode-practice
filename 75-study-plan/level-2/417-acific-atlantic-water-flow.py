from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def explore(queue, curr):
            nonlocal R, C, seen, directions, heights, result
            while queue:
                node = queue.popleft()
 
                if node not in seen:
                    seen[node] = [False, False, 0]

                if seen[node][curr]:
                    continue

                seen[node][curr] = True
                seen[node][2] += 1

                if seen[node][2] == 2:
                    result.append(node)

                x, y = node
                for mx, my in directions:
                    nx, ny = x + mx, y + my
                    if 0 <= nx < R and 0 <= ny < C and heights[nx][ny] >= heights[x][y]:
                        queue.append((nx, ny))

        R, C = len(heights), len(heights[0])
        if R == C == 1:
            return [(0, 0)]

        result = []
        queue = deque([])
        seen = {}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for x in range(R):
            queue.append((x, 0))

        for y in range(C):
            queue.append((0, y))

        explore(queue, 0)

        queue = deque([])
        for x in range(R):
            queue.append((x, C-1))

        for y in range(C):
            queue.append((R-1, y))
        explore(queue, 1)
        return result


print(Solution().pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
      2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
