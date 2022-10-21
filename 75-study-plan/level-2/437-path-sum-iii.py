# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def calcuate(node, total):
            nonlocal counter, targetSum, prefix_sum

            if node == None: return

            total += node.val

            if total == targetSum:
                counter += 1

            counter += prefix_sum[total - targetSum]
            prefix_sum[total] += 1

            calcuate(node.left, total)
            calcuate(node.right, total)
            
            prefix_sum[total] -= 1

        counter = 0
        prefix_sum = defaultdict(lambda: 0)
        calcuate(root, 0)
        return counter