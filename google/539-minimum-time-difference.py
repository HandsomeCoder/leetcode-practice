from typing import List


class Solution:
    cache = {}
    def findMinDifference(self, timePoints: List[str]) -> int:


        def convert_hours_to_mins(hr):
            if hr not in self.cache:
                self.cache[hr] = int(hr) * 60
            return self.cache[hr]

        points = set()
        for idx, point in enumerate(timePoints):
            if point in points:
                return 0

            h, m = point.split(":")        
            timePoints[idx] = convert_hours_to_mins(h) + int(m)
            points.add(point)

        timePoints.sort()
        tln = len(timePoints)
        round_by = 24 * 60
        min_difference = round_by + 1
                
        for idx in range(1, tln):
            min_difference = min(min_difference, timePoints[idx] - timePoints[idx-1])

        return min(min_difference, (round_by + timePoints[0]) - timePoints[-1])

