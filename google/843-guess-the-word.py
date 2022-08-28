# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
from collections import Counter, defaultdict
from typing import List


class Master:
    def guess(self, word: str) -> int:
        return 1


class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:


        words.sort()
        match_count, idx, aln = 0, 0, len(words)
        blacklisted_letters = [set() for _ in range(6)]

        for idx in range(aln):
            is_p_word = True
            word = words[idx]
            for idx, wch in enumerate(word):
                if wch in blacklisted_letters[idx]:
                    is_p_word = False
                    break

            if not is_p_word:
                continue

            if match_count > 0:
                is_p_word = False
                for wlch, wch in zip(whitelisted_word, word):
                    if wch == wlch:
                        is_p_word = True
                        break

            if not is_p_word:
                continue


            count = master.guess(word)
            
            if count == 0:
                for idx, wch in enumerate(word):
                    blacklisted_letters[idx].add(wch)
            elif count > match_count:
                match_count = count
                if match_count == 6:
                    break

                whitelisted_word = word

print(Solution().findSecretWord(
    ["acckzz", "ccbazz", "eiowzz", "abcczz"], Master()))
