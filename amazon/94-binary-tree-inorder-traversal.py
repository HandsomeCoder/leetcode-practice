# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def get_inorder(node, result):
            if node == None:
                return

            get_inorder(node.left, result)
            result.append(node.val)
            get_inorder(node.right, result)

        result = []
        get_inorder(root, result)
        return result
