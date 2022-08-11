from collections import defaultdict, deque
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        result = []

        def build_path(src):
            neighbours = graph[src]

            while neighbours:
                build_path(neighbours.pop())

            result.append(src)

        for src, dest in tickets:
            graph[src].append(dest)

        for _, values in graph.items():
            values.sort(reverse=True)

        node = "JFK"
        build_path(node)

        return result[::-1]


print(Solution().findItinerary(
    [["MEL", "PER"], ["SYD", "CBR"], ["AUA", "DRW"], ["JFK", "EZE"], ["PER", "AXA"], ["DRW", "AUA"], ["EZE", "SYD"], ["AUA", "MEL"], ["DRW", "AUA"], ["PER", "ANU"], ["CBR", "EZE"], ["EZE", "PER"], ["MEL", "EZE"], ["EZE", "MEL"], ["EZE", "TBI"], ["ADL", "DRW"], ["ANU", "EZE"], ["AXA", "ADL"]]))
