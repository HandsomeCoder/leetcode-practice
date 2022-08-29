from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        # def is_subsequence(l, r, base_letter_count, base, word):           
        #     if l == -1 or r == -1:
        #         return False

        #     idx, wln = 0, len(word)
        #     if wln > (r - l + 1):
        #         return False

        #     word_counter = defaultdict(lambda: 0)
        #     for wch in word:
        #         word_counter[wch] += 1
        #         if word_counter[wch] > base_letter_count[wch]:
        #             return False

        #     for b_idx in range(l, r+1):
        #         if base[b_idx] == word[idx]:
        #             idx += 1
        #             if idx == wln:
        #                 return True
        #     return False

        # start_idx, end_idx = defaultdict(lambda: -1), defaultdict(lambda: -1)
        # count, letter_count = 0,  defaultdict(lambda: 0)

        # for idx, sch in enumerate(s):
        #     if sch not in start_idx:
        #         start_idx[sch] = idx
        #     end_idx[sch] = idx
        #     letter_count[sch] += 1

        # cache = set()
        # for word in words:
        #     if word in cache:
        #         count += 1
        #     elif is_subsequence(start_idx[word[0]], end_idx[word[-1]], letter_count, s, word):
        #         cache.add(word)
        #         count += 1

        cache = {}
        def index(ch):
            if ch not in cache:
                cache[ch] = ord(ch) - ord("a")
            
            return cache[ch]

        storage = [[] for _ in range(26)]
        count = 0

        for word in words:
            itr = iter(word)
            storage[index(next(itr))].append(itr)

        for sch in s:
            match_words = storage[index(sch)]
            storage[index(sch)] = []

            for word_itr in match_words:
                nxt_ch = next(word_itr, None)
                if nxt_ch == None:
                    count += 1
                else:
                    storage[index(nxt_ch)].append(word_itr) 

        return count
