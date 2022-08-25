from collections import defaultdict
from email.policy import default
from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_word_count = Counter(s)

        t_word_count = defaultdict(lambda: 0)
        for tch in t:
            t_word_count[tch] += 1
            if t_word_count[tch] > s_word_count.get(tch, 0):
                return False

        return True