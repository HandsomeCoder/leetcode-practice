from typing import List


class Solution:
    def minimumHealth(self, damages: List[int], armor: int) -> int:
        total = 0
        max_value = damages[0]

        for damage in damages:
            total += damage
            max_value = max(max_value, damage)

        return total - min(max_value, armor) + 1