from collections import defaultdict
from heapq import heapify, nsmallest
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(lambda: 0)
        for num in nums:
            counter[num] += 1

        
        frequency = [(-v, k) for k, v in counter.items()]
        if len(frequency) == k:
            return [x for _, x in frequency]


        heapify(frequency)

        return [x for _, x in nsmallest(k, frequency)]
