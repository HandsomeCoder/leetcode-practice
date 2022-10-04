from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def generate_valid_str(s, curr, idx, open_cnt, skip, result):
            nonlocal close_counter, min_skip

            if skip > min_skip:
                return
            elif len(s) == idx:
                if open_cnt == 0:
                    result.add(curr)
                    min_skip = min(skip, min_skip)
                return

            generate_valid_str(s, curr, idx + 1, open_cnt, skip + 1, result)            
            sch = s[idx]
            if sch == "(":
                open_cnt += 1
            elif sch == ")":
                open_cnt -= 1
            if open_cnt >= 0 and open_cnt <= close_counter[idx]:
                generate_valid_str(s, curr + sch, idx + 1, open_cnt, skip, result)

        sln = len(s)
        min_skip = sln
        close_counter = [0 for _ in range(sln)]
        close_cnt = 0 
        for idx in range(sln-1, -1, -1):
            if s[idx] == ")":
                close_cnt += 1
            close_counter[idx] = close_cnt

        valid_result = set()
        generate_valid_str(s, "", 0, 0, 0, valid_result)

        min_length = sln - min_skip
        return list(filter(lambda x: len(x) >= min_length, valid_result))


print(Solution().removeInvalidParentheses("p(r)"))
