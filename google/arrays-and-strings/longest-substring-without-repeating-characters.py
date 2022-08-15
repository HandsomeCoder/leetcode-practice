class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ln = len(s)

        if ln == 0 or ln == 1:
            return ln
        
        char_visited = [False] * 26
        
        unicode_a = ord("a")

        left = 0
        max_seq_len = -1
        for right in range(ln):
            sch = s[right]

            if char_visited[ord(sch) - unicode_a]:
                max_seq_len = max(max_seq_len, right - left)
                while True:
                    prev = s[left]
                    char_visited[ord(prev) - unicode_a] = False                    
                    left += 1

                    if prev == sch:
                        break


            char_visited[ord(sch) - unicode_a] = True

        return max(max_seq_len, ln - left)
    