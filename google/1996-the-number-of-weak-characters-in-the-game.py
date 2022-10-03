from collections import defaultdict, deque
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:

        properties.sort(key=lambda x: (-x[1], x[0]))
        mapping = defaultdict(list)
        unique_attacks = []
        for a, d in properties:
            if a not in mapping:
                unique_attacks.append(a)

            mapping[a].append(d)

        ln = len(unique_attacks)

        if ln == 1:
            return 0

        unique_attacks.sort()
        defences = deque(mapping[unique_attacks[0]])

        cnt = 0
        for idx in range(1, ln):
            itr = mapping[unique_attacks[idx]]
            while defences and defences[-1] < itr[0]:
                defences.pop()
                cnt += 1
            
            for d in itr:
                defences.append(d)
        
        return cnt