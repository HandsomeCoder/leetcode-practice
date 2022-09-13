from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        points = list(map(tuple, [p1, p2, p3, p4]))

        if len(set(points)) != 4:
            return False

        def get_distance(one, two):
            x, y = one
            a, b = two
            return pow(x-a, 2) + pow(y-b, 2)

        distances = set()

        for i in range(4):
            for j in range(i+1, 4):
                distances.add(get_distance(points[i], points[j]))
        
        return len(distances) == 2