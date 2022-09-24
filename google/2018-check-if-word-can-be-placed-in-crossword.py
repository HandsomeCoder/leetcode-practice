from typing import List


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def get(r, c):
            if 0 <= r < R and 0 <= c < C:
                return board[r][c]
            return "#"

        def check_horizontal(x, y, cln, word):
            wln = len(word)
            row = board[x]

            if get(x, y - 1) != "#" or y + wln > cln or get(x, y + wln) != "#":
                return False

            valid = True
            for idx in range(wln):
                value = word[idx] if row[y + idx] == " " else row[y + idx]
                if value != word[idx]:
                    valid = False
                    break

            if valid:
                return True

            ln = wln - 1
            for idx in range(wln):
                value = word[ln-idx] if row[y + idx] == " " else row[y + idx]
                if value != word[ln-idx]:
                    return False
            return True

        def check_vertical(x, y, rln, word):
            wln = len(word)
            if get(x - 1, y) != "#" or x + wln > rln or get(x + wln, y) != "#":
                return False

            valid = True
            for idx in range(wln):
                value = word[idx] if board[x +
                                           idx][y] == " " else board[x+idx][y]
                if value != word[idx]:
                    valid = False
                    break

            if valid:
                return True

            ln = wln - 1
            for idx in range(wln):
                value = word[ln-idx] if board[x +
                                              idx][y] == " " else board[x+idx][y]
                if value != word[ln-idx]:
                    return False
            return True

        for r in range(R):
            for c in range(C):
                itr = board[r][c]
                if itr != "#" and (check_horizontal(r, c, C, word) or check_vertical(r, c, R, word)):
                    return True

        return False


# print(Solution().placeWordInCrossword(
#     board=[["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word="abc"))
# print(Solution().placeWordInCrossword(
#     board=[[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word="ac"))
# print(Solution().placeWordInCrossword(
#     [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], "ca"))
print(Solution().placeWordInCrossword(
    [["#", "#", "#"], ["#", "#", "#"], ["#", " ", "c"]], "ca"))
