from collections import defaultdict
from operator import ne
from typing import List


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        cache = {}
        def get_path(src, dest, visited):

            if src in cache and cache[src]:
                return True

            if src == dest:
                return True

            if len(graph[src]) == 0:
                return False
            
            for neigh in graph[src]:

                if neigh in visited:
                    return False

                visited.add(neigh)
                if not get_path(neigh, dest, visited):
                    return False
                visited.remove(neigh)

            cache[src] = True
            return True



        for src, dest in edges:
            graph[src].append(dest)

        if len(graph[source]) == 0:
            return source == destination

        if destination in graph:
            return False


        visited = set()
        visited.add(source)
        for neigh in graph[source]:
            visited.add(neigh)
            if not get_path(neigh, destination, visited):
                return False
            visited.remove(neigh)

        return True



        # graph = defaultdict(list)

        # cache = {}

        # def get_path(src, dest, visited):

        #     if src == dest:
        #         return True

        #     if src in visited:
        #         return False

        #     visited.add(src)
        #     for idx, neigh in enumerate(graph[src]):
        #         # if visited[src][idx]:
        #         #     continue

        #         # visited[src][idx] = True
        #         if not get_path(neigh, dest, visited):
        #         # visited[src][idx] = False
        #             return False

        #     return False

        # for src, dest in edges:
        #     graph[src].append(dest)

        # if len(graph[destination]) != 0:
        #     return False

        # visited = set()
        # # for key, values in graph.items():
        # #     visited[key] = [False] * len(values)

        # visited.add(source)
        # for idx, neigh in enumerate(graph[source]):

        #     if not get_path(neigh, destination, visited):
        #         return False

        # return True


        


print(Solution().leadsToDestination(
    3,
    [[0, 1], [1, 1], [1, 2]], 0, 2))
