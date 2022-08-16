from collections import defaultdict, deque
from typing import Counter, List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_counter = Counter(words)

        sln = len(s)
        wl = len(words[0])
        target = len(words)
        min_length = wl * target
        
        if sln < min_length:
            return []

        s_words = []
        idxWordMap = {}

        for i in range(wl):
            for idx in range(i, sln, wl):
                sch = s[idx: idx+wl]

                if sch in word_counter:
                    s_words.append(idx)
                    idxWordMap[idx] = sch

        s_words.sort()

        if target == 1:
            return s_words

        result = []
        for idx in s_words:
            if min_length + idx > sln:
                break

            buffer = defaultdict(lambda: 0)
            match = True
            word_idx = idx 
            for _ in range(target):    
                if word_idx not in idxWordMap:
                    match = False
                    break

                word = idxWordMap[word_idx]
                buffer[word] += 1

                if buffer[word] > word_counter[word]:
                    match = False
                    break

                word_idx += wl

            if match:
                result.append(idx)

        return result