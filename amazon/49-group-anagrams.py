from collections import defaultdict
from typing import Counter, List


class Solution:
    cache = {}
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def generate_key(word):
            if word in self.cache:
                return self.cache[word]

            counter = [0 for _ in range(26)]
            for wch in word:
                counter[ord(wch)-97] += 1
            
            self.cache[word] = tuple(counter)
            return self.cache[word]

        group = defaultdict(list)
        for itr in strs:
            group[generate_key(itr)].append(itr)

        return group.values()