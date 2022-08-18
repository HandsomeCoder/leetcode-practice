# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        if startValue == destValue:
            return ""

        def get_path(node, target, path):
            if node == None:
                return False

            if node.val == target:
                return True

            left = get_path(node.left, target, path)
            if left:
                path.append("L")
                return True

            right = get_path(node.right, target, path)
            if right:
                path.append("R")
                return True

            return False

        s_path, d_path = [], []
        get_path(root, startValue, s_path)
        get_path(root, destValue, d_path)

        s_path = s_path[::-1]
        d_path = d_path[::-1]

        diff_move_idx = 0
        for s, d in zip(s_path, d_path):
            diff_move_idx += 1
            if s != d:
                break

        sln, dln = len(s_path), len(d_path)
        if sln == 0:
            return "".join(d_path)

        if dln == 0:
            return "U" * sln 

        # different sub-tree
        return "U" * (sln - diff_move_idx) + "".join(d_path[diff_move_idx:])
