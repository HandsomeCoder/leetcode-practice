from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        def identify_cluster(x, y, no):
            nonlocal cluster_map
            cluster_map[no] = get_island_size(x, y, no, 1)

        def get_island_size(x, y, cluster, size):
            nonlocal grid, R, C
            grid[x][y] = cluster

            max_size = size
            for nx, ny in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
                if 0 <= nx < R and 0 <= ny < C:
                    if grid[nx][ny] == 1:
                        max_size = max(max_size, get_island_size(
                            nx, ny, cluster, max_size + 1))
            return max_size

        def get_near_by_island(x, y):
            nonlocal cluster_id, cluster_map
            islands = []
            visited_island = set()
            for nx, ny in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
                if 0 <= nx < R and 0 <= ny < C:
                    if grid[nx][ny] == 1:
                        identify_cluster(nx, ny, cluster_id)
                        cluster_id += 10

                    cid = grid[nx][ny]
                    if grid[nx][ny] >= 10 and cid not in visited_island:
                        visited_island.add(cid)
                        islands.append(cluster_map[cid])

            return islands

        R, C = len(grid), len(grid[0])
        max_p_size = R * C

        cluster_id = 10
        no_water = True
        max_size = 0
        cluster_map = {}
        for x in range(R):
            for y in range(C):
                if grid[x][y] == 0:
                    no_water = False
                    islands = get_near_by_island(x, y)
                    islands.sort()
                    max_size = max(max_size, sum(islands) + 1)

        return max_p_size if no_water else max_size
