import random
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def partition(left, right, pivot_index):
            pivot = points[pivot_index][0]

            points[pivot_index], points[right] = points[right], points[pivot_index]

            swap_idx = left
            for i in range(left, right):
                if points[i][0] < pivot:
                    if i != swap_idx:
                        points[i], points[swap_idx] = points[swap_idx], points[i]
                    swap_idx += 1

            points[swap_idx], points[right] = points[right], points[swap_idx]

            return swap_idx

        def arrange(left, right, k_smallest):
            
            if left >= right: return

            pivot_idx = partition(left, right, random.randint(left, right))

            if pivot_idx > k_smallest:
                arrange(left, pivot_idx - 1, k_smallest)
            elif pivot_idx < k_smallest:
                arrange(pivot_idx + 1, right, k_smallest)


        if len(points) == k:
            return points
                
        points = [((point[0] * point[0]) + (point[1] * point[1]), (point[0], point[1])) for point in points]
        
        if k == 1:
            return [min(points, key=lambda x: x[0])[1]]
        
        arrange(0, len(points) - 1, k)
        return list(map(lambda x: x[1], points[:k]))                         
