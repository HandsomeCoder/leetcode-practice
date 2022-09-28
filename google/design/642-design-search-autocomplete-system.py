from collections import deque
from typing import List


class Trie:

    def __init__(self) -> None:
        self.children = {}
        self.is_word = False
        self.weight = 0

    def insert(self, word, weight):
        itr = self
        for wch in word:
            if wch not in itr.children:
                itr.children[wch] = Trie()
            itr = itr.children[wch]

        itr.is_word = True
        itr.weight += weight

    def is_prefix(self, prefix):
        itr = self
        for pch in prefix:
            if pch not in itr.children:
                return (False, None)
            itr = itr.children[pch]
        return (True, itr)

    def all_words(self, word, result):
        itr = self
        if itr.is_word:
            result.append((itr.weight, "".join(word)))

        for kch, value in itr.children.items():
            word.append(kch)
            value.all_words(word, result)
            word.pop()


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.curr_str = ""
        self.is_word = False

        for idx, sentence in enumerate(sentences):
            self.trie.insert(sentence, times[idx])

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.insert(self.curr_str, 1)
            self.curr_str = ""
            return []

        self.curr_str += c
        prefix, node = self.trie.is_prefix(self.curr_str)
        if not prefix:
            return []

        words = []
        node.all_words(deque([self.curr_str]), words)
        words.sort(key=lambda x: (-x[0], x[1]))
        return [x[1] for x in words[:3]]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
