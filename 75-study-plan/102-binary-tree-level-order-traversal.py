from typing import List, Optional
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        result = [[root.val]]
        stack = deque([(root, 1)])
        ln = 0

        while stack:
            itr, idx = stack.pop()

            value = []

            if itr.right:
                value.append(itr.right.val)
                stack.append((itr.right, idx + 1))
            
            if itr.left:
                value.append(itr.left.val)
                stack.append((itr.left, idx + 1))

            if not value:
                continue

            value.reverse()
            if idx <= ln:
                result[idx].extend(value)
            else:
                result.append(value)
                ln += 1

        return result
