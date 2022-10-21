from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build_tree(l, r, nums):
            if l > r:
                return None

            if l == r:
                return TreeNode(nums[l])
            
            m = (l+r) // 2
            left = build_tree(l, m-1, nums)
            right = build_tree(m+1, r, nums)

            return TreeNode(nums[m], left, right)

        ln = len(nums)
        if ln == 1:
            return TreeNode(nums[0])

        l, r = 0, len(nums) - 1
        return build_tree(l, r, nums)