from collections import defaultdict, deque
from math import floor, sqrt
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def explore(graph, src):
            visited = set()
            queue = deque([src])
            count = 0
            while queue:
                next = queue.pop()
                if next in visited:
                    continue
                visited.add(next)
                count += 1
                queue.extend(graph[next])
            return count

        bln = len(bombs)
        graph = defaultdict(set)

        for i in range(bln):
            x, y, r1 = bombs[i]
            for j in range(i+1, bln):
                a, b, r2 = bombs[j]
                d = floor(sqrt(pow((x - a), 2) + pow((y - b), 2)))
                if r1 >= d:
                    graph[i].add(j)
                if r2 >= d:
                    graph[j].add(i)

        for i in range(bln):
            graph[i] = list(graph[i])

        max_count = 1
        for i in range(bln):
            max_count = max(max_count, explore(graph, i))
            if max_count == bln:
                break

        return max_count


print(Solution().maximumDetonation(
    [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))
