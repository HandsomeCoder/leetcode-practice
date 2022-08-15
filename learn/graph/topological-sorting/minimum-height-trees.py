from collections import defaultdict, deque
from multiprocessing import connection
from operator import ne
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]
        elif n == 2:
            return [0, 1]

        graph = defaultdict(list)

        connections = [0] * n
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

            connections[x] += 1
            connections[y] += 1

        leafs = []

        for i, c in enumerate(connections):
            if c == 1:
                leafs.append(i)

        while len(graph) > 2:
            new_leafs = []
            for leaf in leafs:
                connections[leaf] = 0
                for neigh in graph[leaf]:
                    connections[neigh] -= 1
                    if connections[neigh] == 1:
                        new_leafs.append(neigh)

                graph.pop(leaf)

            leafs = new_leafs

        return list(graph.keys())


print(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
print(Solution().findMinHeightTrees(
    6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
