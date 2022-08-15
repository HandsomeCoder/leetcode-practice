from pprint import pprint
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ln = len(matrix)

        if ln == 1:
            return

        # reflect
        for x in range(ln):
            l, r = 0, ln-1
            while l < r:
                matrix[x][l], matrix[x][r] = matrix[x][r], matrix[x][l]
                l += 1
                r -= 1

        # transpose
        for x in range(ln):
            for y in range(x, ln):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]


        pprint(matrix)

        # starts = [(i, i) for i in range(ln // 2)]

        # for sx, sy in starts:
        #     bases = [(sx + (mr * r), sy + (mc * c))
        #              for mr, mc in [(0, 0), (0, 1), (1, 1), (1, 0)]]
        #     corners = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        #     for i in range(ln-1):
        #         indexes = [(xb + (xc * i), yb + (yc * i))
        #                    for (xb, yb), (xc, yc) in zip(bases, corners)]
        #         px, py = indexes[0]
        #         for x, y in indexes[1:]:
        #             matrix[px][py], matrix[x][y] = matrix[x][y], matrix[px][py]

        #     r -= 2
        #     c -= 2
        #     ln -= 2
