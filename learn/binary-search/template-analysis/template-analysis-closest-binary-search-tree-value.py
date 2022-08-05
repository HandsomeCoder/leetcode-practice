# Definition for a binary tree node.
from typing import Optional



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        itr = root
        res = itr.val
        while itr:
            res = min(res, itr.val, key = lambda x: abs(target - x))
            itr = itr.left if itr.val > target else itr.right
        return res
        