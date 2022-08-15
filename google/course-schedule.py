from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        in_degrees = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            in_degrees[b] += 1

        queue = deque([])
        for idx, degree in enumerate(in_degrees):
            if degree == 0:
                queue.append(idx)

        while queue:
            course = queue.popleft()

            for next_course in graph[course]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    queue.append(next_course)

            graph.pop(course)

        return len(graph) == 0


print(Solution().canFinish(
    5,
    [[1, 4], [2, 4], [3, 1], [3, 2]]))
