from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:

        graph = defaultdict(list)

        in_degree = [0] * n
        for prev, next in relations:
            graph[prev].append(next)
            in_degree[next-1] += 1

        queue = deque([])
        for idx, degree in enumerate(in_degree):
            if degree == 0:
                queue.append((idx+1, 1))


        max_semester = -1

        while queue:
            course, semester = queue.popleft()
            max_semester = max(max_semester, semester)

            for next_course in graph[course]:
                in_degree[next_course-1] -= 1
                if in_degree[next_course-1] == 0:
                    queue.append((next_course, semester + 1))

            graph.pop(course)

        return max_semester if len(graph) == 0 else -1