# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def get_height(node, left=True):
            height = 1
            while node:
                height += 1
                node = node.left if left else node.right
            return height

        def exists(node, idx, low, high):
            l, r = low, high
            for _ in range(lh):
                while l <= r:
                    m = (l + r) // 2
                    if m > idx:
                        r = m - 1
                        node = node.left
                    else:
                        l = m + 1
                        node = node.right

            return node != None

        if root == None:
            return 0

        lh, rh = get_height(root.left), get_height(root.right, False)

        nodes_count = pow(2, lh) - 1

        if lh == rh:
            return nodes_count


        leaf_node = pow(2, lh-1)
        nodes_count -= leaf_node


        low, high = 1, leaf_node-1
        l, r = low, high
        while l <= r:
            m = (l + r) // 2
            if exists(root, m, low, high):
                l = m + 1
            else:
                r = m - 1

        return nodes_count + l


print(Solution().countNodes(TreeNode(1, TreeNode(
    2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))))
