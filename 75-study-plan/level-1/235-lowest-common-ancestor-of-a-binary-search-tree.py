# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> 'TreeNode':
        a, b = p.val, q.val
        if b < a:
            a, b = b, a

        while root:
            itr = root.val
            if a <= itr <= b:
                return root
            elif a < itr and b < itr:
                root = root.left
            else:
                root = root.right
                

                    
