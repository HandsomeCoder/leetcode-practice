# 1239-maximum-length-of-a-concatenated-string-with-unique-characters

from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def unicode(ch):
            return ord(ch) - ord('a')

        def is_unique(strs):
            idxs = set()
            for ch in strs:
                uni = unicode(ch)
                if uni in idxs:
                    return None

                idxs.add(uni)    
            return tuple(idxs)

        def merge_valid(hash, char_str, xstr):
            nonlocal cache_merge
            node = (char_str, xstr)
            if node not in cache_merge:
                cache_merge[node] = True
                for i in xstr:
                    if hash[i]:
                        cache_merge[node] = False
                        break

            return cache_merge[node]


        def get_max_ln(idx, charset_hash, curr_len):
            nonlocal valid_set, cache_max_len, ln
            
            if idx == ln or curr_len == 26:
                return curr_len

            char_str = tuple(charset_hash)
            node = (idx, char_str)
            if node not in cache_max_len:
                itr = valid_set[idx]
                with_str = without = get_max_ln(idx + 1, charset_hash, curr_len)
                if without != 26 and merge_valid(charset_hash, char_str, itr):
                    for i in itr:
                        charset_hash[i] = True

                    with_str = get_max_ln(idx + 1, charset_hash, curr_len + len(itr))
                    if with_str == 26:
                        cache_max_len[node] = 26
                        return cache_max_len[node]

                    for i in itr:
                        charset_hash[i] = False

                cache_max_len[node] = max(with_str, without)

            return cache_max_len[node]


        cache_max_len, cache_merge = {}, {}
        min_ln = 0
        valid_set = []

        for itr in arr:
            idxs = is_unique(itr)
            if idxs:
                valid_set.append(idxs)
                min_ln = max(min_ln, len(itr))

        if min_ln == 26:
            return min_ln

        ln = len(valid_set)
        
        return get_max_ln(0, [False for _ in range(26)], 0)
