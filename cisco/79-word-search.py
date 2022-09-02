from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        
        def search(board, row, col, word, idx):
            if board[row][col] != word[idx]:
                return False

            idx += 1
            if len(word) == idx:
                return True

            direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            letter = board[row][col]
            board[row][col] = "#"

            for r, c in direction:
                new_row, new_col = row + r, col + c
                if 0 <= new_row < R and 0 <= new_col < C and board[new_row][new_col] != "#":
                    if search(board, new_row, new_col, word, idx):
                        return True

            board[row][col] = letter
            return False

        for r in range(R):
            for c in range(C):
                if search(board, r, c, word, 0):
                        return True
        return False 


print(Solution().exist(
    [["A"]],
    "A"))
