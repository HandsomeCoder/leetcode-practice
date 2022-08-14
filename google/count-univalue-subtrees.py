from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:

        INVALID_NODE_VALUE = -2000

        def count_validate_subtree(node, count):
            node_value = node.val

            lvalue = rvalue = node_value
            lcount = rcount = count
            lvalid = rvalid = True
            if node.left != None:
                lvalid, lcount, lvalue = count_validate_subtree(node.left, count)

            if node.right != None:
                rvalid, rcount, rvalue = count_validate_subtree(node.right, count)

            count = lcount+rcount
            if not lvalid and not rvalid:
                return (False, count, INVALID_NODE_VALUE)

            if node_value == lvalue and node_value == rvalue:
                return (True, count+1, node_value)
            else:
                return (False, count, INVALID_NODE_VALUE)

        if root == None:
            return 0

        return count_validate_subtree(root, 0)[1]


print(Solution().countUnivalSubtrees(TreeNode(5, TreeNode(5, TreeNode(5), TreeNode(5)),
                                              TreeNode(5, None, TreeNode(5))
                                              )))
