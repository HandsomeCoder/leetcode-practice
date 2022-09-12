from collections import defaultdict
from email.policy import default
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        len_words = defaultdict(list)

        max_len = -1
        for word in words:
            wln = len(word)
            max_len = max(wln, max_len)
            len_words[len(word)].append(word)

        if not len_words[1]:
            return ""

        len_words[1] = set(len_words[1])

        result_word_len = 1
        for idx in range(2, max_len+1):

            valid_words = set()
            for word in len_words[idx]:
                if word[:idx-1] in len_words[idx-1]:
                    valid_words.add(word)

            if not valid_words:
                break

            result_word_len = idx
            len_words[idx] = valid_words

        len_words[result_word_len] = sorted(len_words[result_word_len])
        return len_words[result_word_len][0]