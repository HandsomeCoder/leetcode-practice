from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        def is_connected(one, two):
            for x in two:
                if x in one:
                    return True
            return False

        if source == target:
            return 0

        graph = defaultdict(list)
        ln = len(routes)
        routes_set = []
        
        queue = deque([])
        for i in range(ln):
            route = set(routes[i])
            routes_set.append(route)
            if source in route:
                if target in route:
                    return 1
                queue.append((i, 1))

            for j in range(i+1, ln):
                if is_connected(route, routes[j]):
                    graph[i].append(j)
                    graph[j].append(i)


        visited = set([])
        while queue:
            bus, change = queue.popleft()
            if bus in visited:
                continue

            if target in routes_set[bus]:
                return change

            visited.add(bus)
            for next_bus in graph[bus]:
                queue.append((next_bus, change + 1))

        return -1
