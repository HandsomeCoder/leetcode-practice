from collections import deque
from typing import List


class Trie:
    def __init__(self, words=[]):
        self.children = {}
        self.is_word = False

        for word in words:
            self.insert(word)

    def insert(self, word):
        itr = self
        for wch in word:
            if wch not in itr.children:
                itr.children[wch] = Trie()

            itr = itr.children[wch]
        itr.is_word = True

    def start_with(self, prefix) -> bool:
        itr = self
        for wch in prefix:
            if wch not in itr.children:
                return (False, False)

            itr = itr.children[wch]
        return (True, itr.is_word)

    def delete(self, itr, word, wln):
        if wln == 0:
            itr.is_word = False
            return

        wch = word[0]
        self.delete(itr.children[wch], word[1:], wln - 1)

        if not itr.children[wch].is_word and len(itr.children[wch].children) == 0:
            itr.children.pop(wch)

    def remove_word(self, word) -> bool:
        itr = self
        self.delete(itr, word, len(word))


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def find_word(trie, r, c, prefix, r_words):
            if len(trie.children) == 0:
                return

            exist, is_word = trie.start_with(prefix)
            if is_word:
                r_words.append(prefix)
                trie.remove_word(prefix)

            if exist:
                ch = board[r][c]
                board[r][c] = "#"
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for x, y in directions:
                    if len(trie.children) == 0:
                        return
                    mr = r + x
                    mc = c + y
                    if 0 <= mr < R and 0 <= mc < C and board[mr][mc] != "#":
                        find_word(trie, mr, mc, prefix +
                                  board[mr][mc], r_words)
                board[r][c] = ch

        trie = Trie(words)
        R, C = len(board), len(board[0])
        result = []
        for r in range(R):
            for c in range(C):
                r_words = deque([])
                find_word(trie, r, c, board[r][c], r_words)
                if r_words:
                    result.extend(r_words)

                if len(trie.children) == 0:
                    break

        return result


print(Solution().findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                           ["oath", "pea", "eat", "rain"]))
