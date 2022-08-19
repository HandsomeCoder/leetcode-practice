from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        if len(indices) == 0:
            return s

        indices = sorted([(v, i) for i, v in enumerate(indices)])
        ranges, exp_range_idx, s_len = [], 0, len(s)

    
        for index, pos_idx in indices:
            left = right = index
            src = sources[pos_idx]
            m_idx, src_len = 0, len(src)

            match_length = min(s_len - right, src_len)
            while m_idx < match_length:
                if s[right] != src[m_idx]:
                    break
                right += 1
                m_idx += 1

            if right - left != src_len:
                continue

            if left != exp_range_idx:
                ranges.append((exp_range_idx, left, None))

            ranges.append((left, right, targets[pos_idx]))
            exp_range_idx = right

        if exp_range_idx < s_len:
            ranges.append((exp_range_idx, s_len, None))

        substr = [s[l:r] if t == None else t for l, r, t in ranges]

        return "".join(substr)
