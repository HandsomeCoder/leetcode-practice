class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        visited = set()
        l = len(s)
        for idx in range(l):
            sch = s[idx]
            tch = t[idx]
            if sch not in mapping and tch not in visited:
                visited.add(tch)
                mapping[sch] = tch

            if sch not in mapping or tch != mapping[sch]:
                return False
        
        return True


