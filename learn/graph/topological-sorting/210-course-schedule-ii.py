# 210-course-schedule-ii

from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegrees = defaultdict(lambda: 0)

        queue = deque([])

        for t, s in prerequisites:
            graph[s].append(t)
            indegrees[t] += 1

        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)

        result = []
        visited = [False] * numCourses
        while queue:
            course = queue.popleft()

            if visited[course]:
                continue

            visited[course] = True

            result.append(course)

            for neigh in graph[course]:
                indegrees[neigh] -= 1
                if indegrees[neigh] == 0:
                    queue.append(neigh)

        return result if len(result) == numCourses else []
