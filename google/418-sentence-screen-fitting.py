from shutil import move
from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        moves = []
        for word in sentence:
            move = 0
            for _ in word:
                moves.append(move)
                move -= 1
            moves.append(1)

        cursor = 0
        ln = len(moves)
        for _ in range(rows):
            cursor += cols
            cursor += moves[cursor % ln]
        return cursor // ln
