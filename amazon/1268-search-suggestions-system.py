from collections import deque
from typing import List


class Trie:
    def __init__(self, words=None):
        self.children = {}
        self.is_word = False
        self.seq_arr = []

        if words:
            for word in words:
                self.insert(word)

    def get_seq_arr(self):
        if not self.seq_arr:
            for sch in [chr(idx) for idx in range(97, 123)]:
                self.seq_arr.append(sch)

        return self.seq_arr

    def insert(self, word):
        itr = self
        for wch in word:
            if wch not in itr.children:
                itr.children[wch] = Trie()
            itr = itr.children[wch]
        itr.is_word = True

    def get_words(self, itr, result, rln, current):
        if itr.is_word:
            result.append("".join(current))
            if len(result) == rln:
                return

        for sch in itr.get_seq_arr():
            if sch in itr.children:
                current.append(sch)
                self.get_words(itr.children[sch], result, rln, current)
                current.pop()
                if len(result) == rln:
                    return

    def start_with(self, prefix):
        itr = self
        for wch in prefix:
            if wch not in itr.children:
                itr = None
                break
            itr = itr.children[wch]

        if itr == None:
            return []

        result = []
        self.get_words(itr, result, 3, deque(list(prefix)))
        return result


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        pln = len(products)
        sln = len(searchWord)
        trie = Trie(products)

        result = []
        if pln == 1:
            return [products if searchWord == products[0] else []] * sln 
        
        for idx in range(len(searchWord)):
            result.append(trie.start_with(searchWord[0:idx+1]))

        return result


print(Solution().suggestedProducts(
    ["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
