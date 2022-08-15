from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        max_water = -1
        distance = right - left
        while left < right:
            l_height, r_height = height[left], height[right]
            
            if l_height > r_height:
                max_water = max(max_water, distance * r_height)
                right -= 1
            else:
                max_water = max(max_water, distance * l_height)
                left += 1

        
            distance -= 1
        return max_water

print(Solution().maxArea( [2,3,4,5,18,17,6]))