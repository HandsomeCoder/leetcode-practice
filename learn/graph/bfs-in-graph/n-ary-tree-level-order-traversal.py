# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from collections import deque
from typing import List


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        result = []
        if root is None:
            return result

        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()

            if level == len(result):
                result.append([])


            result[level].append(node.val)

            for child in node.children:
                queue.append((child, level + 1))

        return result

   g     