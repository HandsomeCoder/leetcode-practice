# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check(node):
            if node == None:
                return (True, 0)
            
            lvalid, left = check(node.left)
            if not lvalid:
                return (False, -1)

            rvalid, right = check(node.right)
            if not rvalid:
                return (False, -1)

            if abs(left - right) > 1:
                return (False, -1) 

            return (True, max(left, right) + 1)

        valid, _ = check(root)

        return valid