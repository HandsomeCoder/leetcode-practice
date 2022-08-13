from collections import defaultdict
from typing import Counter, List



class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        wordCounter = Counter(words)

        word_freqs = set()
        levels = defaultdict(list)
        for item, count in wordCounter.items():
            levels[count].append(item)
            word_freqs.add(count)

        result = []
        word_freqs = list(word_freqs)
        word_freqs.sort(reverse=True)

        for count in  word_freqs:
            limit = min(len(levels[count]), k)
            levels[count].sort()
            result.extend(levels[count][:limit])
            k -= limit
            if k == 0:
                break

        return result


print(Solution().topKFrequent(

    ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
    4))
