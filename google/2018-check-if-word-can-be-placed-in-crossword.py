from collections import defaultdict
from typing import List


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        letter_idx = defaultdict(list)
        for idx, wch in enumerate(word):
            letter_idx[wch].append(idx)

        R, C = len(board), len(board[0])

        for r in range(R):
            for c in range(C):
                if board[r][c] in letter_idx:
                    l = r = c
                    while l >= 0 and r < C:
                        if board[r][l] == ""
