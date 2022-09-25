from typing import List

class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:

        def find_match(grid, girls, boy, matching, not_seen):
            for girl in grid[boy]:
                if not_seen[girl]: 
                    not_seen[girl] = False
 
                    if matching[girl] == -1 or find_match(grid, girls, matching[girl], matching, not_seen):
                        matching[girl] = boy
                        return True
            return False
 
        boys, girls = len(grid), len(grid[0])
        matching = [-1] * girls
        result = 0

        for boy in range(boys):
            not_seen = [True] * girls

            values = []
            for idx in range(girls):
                if grid[boy][idx] == 1:
                    values.append(idx)
            
            grid[boy] = values

            if find_match(grid, girls, boy, matching, not_seen):
                result += 1

        return result