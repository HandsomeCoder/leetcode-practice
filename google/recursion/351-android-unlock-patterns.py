class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        matrix = [[5, 7, 5], [7, 8, 7], [5, 7, 5]]

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0),
                     (1, 2), (2, 1), (-1, -2), (-2, -1)]

        def explore(r, c, ln, max_ln):
            if ln == max_ln:
                



        explore(0, 0, 1, ln)
        explore(0, 1, 1, ln)
        explore(1, 1, 1, ln)
