from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        nrow, ncol = len(image) - 1, len(image[0]) - 1

        init_color = image[sr][sc]
        if init_color == color: return image

        visited = set()
        stack = deque([(sr, sc)])

        while stack:
            itr = stack.pop()
            
            if itr in visited:
                continue
            
            visited.add(itr)

            i, j = itr
            image[i][j] = color

            if i > 0 and image[i-1][j] == init_color: 
                stack.append((i-1, j))
            if i < nrow and image[i+1][j] == init_color: 
                stack.append((i+1, j))
            if j > 0 and image[i][j-1] == init_color: 
                stack.append((i, j-1))
            if j < ncol and image[i][j+1] == init_color: 
                stack.append((i, j+1))

        return image