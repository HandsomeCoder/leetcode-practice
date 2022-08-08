from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        def populate_result(node, result):

            if node == None:
                return -1

            height = max(populate_result(node.left, result), populate_result(node.right, result)) + 1

            if height >= len(result):
                result.append([])

            result[height].append(node.val)

            return height


        result = []
        populate_result(root, result)
        return result