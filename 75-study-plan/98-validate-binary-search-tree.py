from math import inf
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, details):

            limit, is_valid = details
            if not is_valid:
                return (limit, False)


            if node.left:
                limit, is_valid = validate(node.left, details)

            print(node.val, limit)
            if is_valid and node.val > limit:
                limit = node.val
            else: 
                return (limit, False)
            
            if node.right:
                limit, is_valid = validate(node.right, (limit, is_valid))

            return (limit, is_valid)
        
        return validate(root, (-inf, True))[1]

