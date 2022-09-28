# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):

        if root == None:
            return ""

        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node == None:
                result.append('')
                continue

            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        return ",".join(result)

    def deserialize(self, data):
        if len(data) == 0:
            return None

        data = data.split(',')
        dln = len(data)
        r = 1
        root = TreeNode(data[0])
        queue = deque([root])

        while r < dln:
            itr = queue.popleft()

            if itr == None:
                continue

            itr.left = None if data[r] == '' else TreeNode(data[r])
            queue.append(itr.left)
            r += 1

            itr.right = None if data[r] == '' else TreeNode(data[r])
            queue.append(itr.right)
            r += 1

        return root
