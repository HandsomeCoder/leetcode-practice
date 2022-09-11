from re import search
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        R, C = len(board), len(board[0])
        cnt = 0
        def prev_r(board, x, y): return x == 0 or board[x-1][y] == "."
        def prev_c(board, x, y): return y == 0 or board[x][y-1] == "."
        for r in range(R):
            for c in range(C):
                if board[r][c] == "X" and prev_r(board, r, c) and prev_c(board, r, c):
                    cnt += 1
        return cnt