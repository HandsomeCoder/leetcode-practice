from collections import defaultdict
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        predecessor = defaultdict(lambda: 0)
        words.sort(key=lambda x: len(x))

        max_length = -1
        for word in words:
            length, w_len = 1, len(word)
            for i in range(w_len):
                itr = word[:i] + word[i+1:]
                p_length = 1 + predecessor[itr]
                length = max(length, p_length)
                if length == w_len:
                    break

            max_length = max(length, max_length)
            predecessor[word] = length

        return max_length