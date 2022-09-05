from collections import defaultdict
from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        def generate_combination(arr):
            ln = len(arr)
            if ln < 3:
                return []

            combinations = set([tuple(arr[-3:])])
            for i in range(ln-3):
                for j in range(i+1, ln):
                    for k in range(j+1, ln):
                        combinations.add((arr[i], arr[j], arr[k]))
            return list(combinations)

        
        users = defaultdict(list)
        record = list(zip(timestamp, website, username))
        record.sort()

        for _, web, user in record:
            users[user].append(web)

        patterns = defaultdict(lambda: 0)
        max_overlap_count = -1
        for user, visits in users.items():
            for pattern in generate_combination(visits):
                patterns[pattern] += 1
                max_overlap_count = max(max_overlap_count, patterns[pattern])

        max_score_pattern = []
        for pattern, count in patterns.items():
            if count == max_overlap_count:
                max_score_pattern.append(pattern)

        if len(max_score_pattern) > 1:
            max_score_pattern.sort() 

        return max_score_pattern[0]