from collections import defaultdict
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, time in times:
            graph[u].append((v, time))

        queue = [(0, k)]
        heapify(queue)
        visited = [False] * n
        max_time = 0
        connected_elements = n

        min_time_for_node = [200] * n
        while queue:
            if connected_elements == 0:
                break

            curr_time, node = heappop(queue)

            if visited[node - 1]:
                continue

            visited[node - 1] = True
            max_time = max(max_time, curr_time)
            connected_elements -= 1
            
            for neigh, time in graph[node]:
                neigh_time = curr_time + time

                if min_time_for_node[neigh-1] > neigh_time:
                    min_time_for_node[neigh-1] = neigh_time
                    heappush(queue, (curr_time + time, neigh))

        return max_time if connected_elements == 0 else -1


print(Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]],
                                  4,
                                  2))
