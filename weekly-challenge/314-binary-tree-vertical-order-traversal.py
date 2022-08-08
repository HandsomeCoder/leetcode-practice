from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return []
        
        queue = deque([(root, 0)])
        result = [[] for _ in range(20)]
        min_idx = 19
        max_idx = 0
        while queue:
            node, idx = queue.popleft()

            if node.left:
                queue.append((node.left, idx - 1))
            
            if node.right:
                queue.append((node.right, idx + 1))

            idx = (10 + idx) if idx >= 0 else (10 - abs(idx)) 
        
            min_idx = min(idx, min_idx)
            max_idx = max(idx, max_idx)
            result[idx].append(node.val)

        return [result[idx] for idx in range(min_idx, max_idx + 1)]          
