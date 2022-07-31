class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sl = len(s)
        si = 0

        if sl == 0:
            return True

        for tch in t:
            sch = s[si]

            if tch == sch:
                si += 1
                if  si == sl:
                    return True
                    
        return False