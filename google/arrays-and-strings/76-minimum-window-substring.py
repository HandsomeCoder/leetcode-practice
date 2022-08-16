from collections import defaultdict, deque
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sln, tln = len(s), len(t)

        if tln > sln:
            return ""

        char_counter = Counter(t)

        min_length = sln + 1

        buffer_counter = defaultdict(lambda: 0)
        queue = deque([])
        match_char = 0
        left = right = -1
        curr_left = 0
        
        
        idx = 0
        while idx < sln:
            sch = s[idx]

            if sch in char_counter:
                buffer_counter[sch] += 1
                queue.append(idx)
                if char_counter[sch] == buffer_counter[sch]:
                    match_char += char_counter[sch] 
                
                if match_char == tln:
                    while queue:
                        curr_left = queue[0]
                        l_sch = s[curr_left]
                        if buffer_counter[l_sch] - 1 < char_counter[l_sch]:
                            break
                        
                        buffer_counter[l_sch] -= 1
                        queue.popleft()

                    curr_min_length = (idx - curr_left) + 1
                    if curr_min_length < min_length:
                        min_length = curr_min_length
                        left, right = curr_left, idx

            idx += 1

        return "" if left == -1 else s[left: right+1]
