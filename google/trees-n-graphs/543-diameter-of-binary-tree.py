# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    max_diameter = -1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def calculate_diameter(node):
            if node == None:
                return 0

            left = calculate_diameter(node.left)
            right = calculate_diameter(node.right)

            self.max_diameter = max(self.max_diameter, left + right)

            return max(left, right) + 1

        if root == None:
            return 0

        calculate_diameter(root)

        return self.max_diameter