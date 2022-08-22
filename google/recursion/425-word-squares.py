from collections import deque
from typing import List


class Trie:
    def __init__(self, words = []):
        self.children = {}
        self.idx = set()
        self.words = words

        for idx, word in enumerate(words):
            self.insert(word, idx)

    def insert(self, word: str, idx: int) -> None:
        itr = self
        for wch in word:
            if wch not in itr.children:
                itr.children[wch] = Trie()

            itr = itr.children[wch]
            itr.idx.add(idx)

    def starts_with(self, prefix: str) -> list:
        itr = self
        for wch in prefix:
            if wch not in itr.children:
                return []
            itr = itr.children[wch]

        return [self.words[idx] for idx in itr.idx]


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        def build_word_square(trie, sln, square, idx, result):

            if len(word) == idx:
                result.append(list(square))
                return

            prefix = "".join([word[idx] for word in square])

            for nextWord in trie.starts_with(prefix):
                square.append(nextWord)
                build_word_square(trie, sln, square, idx+1, result)
                square.pop()


        trie = Trie(words)
        ln = len(words[0])

        result = []
        for word in words:
            build_word_square(trie, ln, deque([word]), 1, result)
        
        return result


print(Solution().wordSquares(["area", "lead", "wall", "lady", "ball"]))
