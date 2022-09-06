from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln == 1:
            return 0 if nums[0] <= 0 else 1

        result = [0 for _ in range(ln+1)]
        negative_count = 0
        neg_num_idx = [-1, -1]
        max_len = -1
        for idx in range(ln):
            num = nums[idx]
            if num == 0:
                negative_count = 0
                neg_num_idx = [-1, -1]
                continue

            if num > 0:
                result[idx] = result[idx-1] + 1
            else:
                if negative_count < 2:
                    neg_num_idx[negative_count] = idx-1

                negative_count += 1
                if negative_count > 1:
                    prev_neg_idx = neg_num_idx[negative_count & 1] 
                    result[idx] = result[prev_neg_idx] + (idx - prev_neg_idx)
                

            max_len = max(max_len, result[idx])

        return max_len