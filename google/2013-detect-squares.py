from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.points_on_x = defaultdict(list)
        self.points_on_y = defaultdict(set)
        self.points = defaultdict(lambda: 0)

    def add(self, point: List[int]) -> None:
        x, y = point
        node = (x, y)
        if node not in self.points:
            self.points_on_x[x].append(y)
            self.points_on_y[y].add(x)
        self.points[node] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        cnt = 0
        for ny in self.points_on_x[x]:
            if ny == y:
                continue

            diff = abs(y - ny)

            for nx in [x + diff, x - diff]:
                if nx in self.points_on_y[y] and (nx, ny) in self.points:
                    cnt += (self.points[(x, ny)] *
                            self.points[(nx, y)] * self.points[(nx, ny)])

        return cnt