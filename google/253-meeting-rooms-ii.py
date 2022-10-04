from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        times = []
        for x, y in intervals:
            times.append((x, 1))
            times.append((y, -1))

        times.sort()
        ln = len(times)

        require = rooms = 0
        for _, event in times:
            require += event
            if require > rooms:
                rooms = require

        return rooms


print(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
