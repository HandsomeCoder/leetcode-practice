# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def get_boundry(node, result, direction):
            if node.left == None and node.right == None:
                return

            if direction:
                result.append(node.val)
                if node.left:
                    return get_boundry(node.left, result)

                if node.right:
                    return get_boundry(node.right, result)

            else:
                if node.right:
                    get_boundry(node.right, result)
                    result.append(node.val)
                    return

                if node.left:
                    get_boundry(node.left, result)
                    result.append(node.val)
                    return

        def get_leaves(node, result):
            if node.left == None and node.right == None:
                result.append(node.val)
                return

            if node.left:
                get_leaves(node.left, result)

            if node.right:
                get_leaves(node.right, result)

        if root == None:
            return []

        boundry = [root.val]
        if root.left:
            get_boundry(root.left, boundry, True)
            get_leaves(root.left, boundry)

        if root.right:
            get_leaves(root.right, boundry)
            get_boundry(root.right, boundry, False)

        return boundry
