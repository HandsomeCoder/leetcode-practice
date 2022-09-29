from collections import defaultdict, deque
from heapq import heapify, heappop, heappush
from typing import List


class AutocompleteSystem:

    def __insert(self, word, weight):
        itr = self.trie
        for wch in word:
            if wch not in itr:
                itr[wch] = {"#": []}
                heapify(itr[wch]["#"])

            itr = itr[wch]
            heappush(itr["#"], (-weight, word))

        self.counter[word] = weight

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = {}
        self.buffer = []
        self.counter = defaultdict(lambda: 0)
        self.match = 0
        self.cursor = self.trie

        for sentence, weight in zip(sentences, times):
            self.__insert(sentence, weight)

    def input(self, c: str) -> List[str]:
        if c == "#":
            word = "".join(self.buffer)
            self.counter[word] += 1
            self.__insert(word, self.counter[word])
            
            self.match = 0
            self.cursor = self.trie
            self.buffer = []
            return []

        result = []
        if c in self.cursor and len(self.buffer) == self.match:
            self.match += 1
            self.cursor = self.cursor[c]
            bucket = deque([])
            while self.cursor["#"] and len(result) < 3:
                weight, sentence = heappop(self.cursor["#"])
                if self.counter[sentence] == -weight:
                    result.append(sentence)
                    bucket.append((weight, sentence))

            while bucket:
                heappush(self.cursor["#"], bucket.pop())

        self.buffer.append(c)
        return result


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
