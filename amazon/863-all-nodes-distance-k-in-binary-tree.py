# Definition for a binary tree node.
from cgitb import reset
from collections import deque
from turtle import st
from typing import List
from unittest import result


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def get_children(start, distance):
            queue = deque(start)
            result = []
            visited = set()
            while queue:
                itr, dist = queue.popleft()
                if itr.val in visited:
                    continue

                if dist == distance:
                    result.append(itr.val)
                    continue

                visited.add(itr.val)

                if itr.left:
                    queue.append((itr.left, dist + 1))
                if itr.right:
                    queue.append((itr.right, dist + 1))
            
            return result

        def search_children(node, value, parents, mapping):
            queue = deque([(node, None)])
            while queue:
                itr, parent = queue.popleft()
                mapping[itr.val] = itr
                parents[itr.val] = parent

                if itr.val == value:
                    return itr

                if itr.left:
                    queue.append((itr.left, itr.val))

                if itr.right:
                    queue.append((itr.right, itr.val))

            return None

        if root == None:
            return []

        if root.val == target.val:
            return get_children([(root, 0)], k)

        parents = {}
        mapping = {}
        node = search_children(root, target.val, parents, mapping)

        if node == None:
            return []

        start = []
        for dist in range(k+1):
            start.append((node, dist))
            parent = parents[node.val]
            if parent == None:
                break
            node = mapping[parent]

        return get_children(start, k)
