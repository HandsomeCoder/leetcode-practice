from math import inf
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    max_path_sum = -inf
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def calculate_max_path(node):

            if node == None:
                return 0

            value = node.val
            left = calculate_max_path(node.left)
            right = calculate_max_path(node.right)

            l_max_path = max(value, left + value, value + right)

            self.max_path_sum = max(self.max_path_sum, l_max_path, left + value + right)

            return l_max_path    

        calculate_max_path(root)

        return self.max_path_sum

# print(Solution().maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))))
print(Solution().maxPathSum(TreeNode(-1, TreeNode(2))))