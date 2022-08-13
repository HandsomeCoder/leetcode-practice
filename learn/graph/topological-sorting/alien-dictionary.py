from collections import defaultdict, deque
from email.policy import default
from itertools import zip_longest
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:

        if len(words) == 1:
            return "".join(set(words[0]))

        graph = defaultdict(set)
        in_degree = {ch: 0 for word in words for ch in word}
        unicode_a = ord("a")

        prev = 0
        for curr in range(1, len(words)):
            p_word = words[prev]
            c_word = words[curr]
            match_found = False

            for pch, cch in zip_longest(p_word, c_word):

                if cch == None and pch != None:
                    return ""

                if pch == None and cch != None:
                    break

                if pch == cch:
                    continue
                
                if cch not in graph[pch]:
                    graph[pch].add(cch)
                    in_degree[cch] += 1
                
                break
            
            prev = curr

        queue = deque([])
        for ch, count in in_degree.items():
            if count == 0:
                queue.append(ch)

        result = []
        visited = [False] * 26
        while queue:
            qch = queue.popleft()
            qch_unicode = ord(qch) - unicode_a

            if visited[qch_unicode]:
                continue

            visited[qch_unicode] = True

            result.append(qch)

            for neigh in graph[qch]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    queue.append(neigh)

        return "".join(result) if len(in_degree) == len(result) else ""


print(Solution().alienOrder(["ac","ab","zc","zb"]))
