from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        def inorder(node, mapping, result):
            if node == None:
                return ""

            order = (inorder(node.left, mapping, result), node.val, inorder(node.right, mapping, result))

            mapping[order] += 1
            if mapping[order] == 2:
                result.append(node)
        
            return order

        mapping = defaultdict(lambda: 0)
        result = []
        inorder(root, mapping, result)
        
        return result