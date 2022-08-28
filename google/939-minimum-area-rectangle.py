from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        x_map = defaultdict(list)
        y_map = defaultdict(list)
        point_set = set()

        for x, y in points:
            point = (x, y)
            x_map[x].append(point)
            y_map[y].append(point)
            point_set.add(point)

        min_area = inf
        visited = set()
        for x, y in points:
            point = (x, y)
            y_coords = x_map[x]
            x_coords = y_map[y]
            visited.add(point)
            if len(y_coords) == 0 or len(x_coords) == 0:
                continue
            
            for y_coord in y_coords:
                if y_coord in visited:
                    continue
                for x_coord in x_coords:
                    if x_coord in visited:
                        continue

                    if (x_coord[0], y_coord[1]) in point_set:
                        area = abs(x_coord[0] - x) * abs(y_coord[1] - y)
                        if area < min_area:
                            min_area = area

        return 0 if min_area == inf else min_area


print(Solution().minAreaRect(
    [[0, 1], [1, 3], [3, 3], [4, 4], [1, 4], [2, 3], [1, 0], [3, 4]]))
