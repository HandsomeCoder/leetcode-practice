# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def is_same(node1, node2):
            if node1 == None and node2 == None:
                return True
            
            if (node1 == None and node2 != None) or  (node2 == None and node1 != None):
                return False

            if node1.val != node2.val:
                return False

            if is_same(node1.left, node2.left) and is_same(node1.right, node2.right):
                return True
        
            return is_same(node1.left, node2.right) and is_same(node1.right, node2.left)

        return is_same(root1, root2)