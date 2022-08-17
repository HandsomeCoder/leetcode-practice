from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_chars = defaultdict(lambda: 0)
        visited = [False] * 26
        unicode_a = ord("a")
        for idx, sch in enumerate(s):
            pos = ord(sch) - unicode_a
            
            if visited[pos]:
                if sch in unique_chars:
                    unique_chars.pop(sch)
                continue
            
            unique_chars[sch] = idx
            visited[pos] = True

        return min(unique_chars.values()) if unique_chars else -1
        