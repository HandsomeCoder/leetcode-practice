from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.cache_sum = {}
        self.updated_cells = {}
        self.updated_count = []

    def update_cache(self, key):
        _, updated_version = self.cache_sum[key]
        if len(self.updated_count) > updated_version:
            while updated_version != len(self.updated_count):
                cell = self.updated_count[updated_version]
                (row, col) = cell 
                (old, val) = self.updated_cells[cell]
                r1, c1, r2, c2 = key
                if r1 <= row <= r2 and c1 <= col <= c2:
                    self.cache_sum[key] = (self.cache_sum[key][0] + (val - old), updated_version)
                updated_version += 1

    def update(self, row: int, col: int, val: int) -> None:
        old = self.matrix[row][col]
        self.matrix[row][col] = val
        cell = (row, col)

        self.updated_count.append(cell)
        if cell in self.updated_cells:
            old = self.updated_cells[cell][0]
        self.updated_cells[cell] = (old, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        range_key = (row1, col1, row2, col2)

        if range_key in self.cache_sum:
            self.update_cache((row1, col1, row2, col2))
            return self.cache_sum[(row1, col1, row2, col2)][0]
        
        total = 0
        for idx in range(row1, row2+1):
            total += sum(self.matrix[idx][col1:col2+1])
        
        self.cache_sum[range_key] = (total, len(self.updated_count))        
        return total