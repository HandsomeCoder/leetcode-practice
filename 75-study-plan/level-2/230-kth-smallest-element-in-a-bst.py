from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def get_k_min(node, k, result):
            if result[1] == k or node == None:
                return

            get_k_min(node.left, k, result)
            if result[1] == k:
                return
            
            result[0] = node.val
            result[1] += 1
            if result[1] == k:
                return

            get_k_min(node.right, k, result)

        result = [0, 0]
        get_k_min(root, k, result)
        return result[0]