from typing import Counter, List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        pair_count = 0
        pair_fruit = -1

        curr_count = 1
        curr_fruit = fruits[0]

        fl = len(fruits)
        max_fruits = -1
        for idx in range(1, fl):
            fruit = fruits[idx]

            if fruit == curr_fruit:
                curr_count += 1

            elif pair_fruit == -1:
                pair_fruit, pair_count = curr_fruit, curr_count
                curr_count, curr_fruit = 1, fruit

            elif fruit == pair_fruit:
                pair_count += curr_count
                pair_fruit = curr_fruit
                curr_count, curr_fruit = 1, fruit

            else:
                max_fruits = max(max_fruits, pair_count + curr_count)
                pair_count, pair_fruit = curr_count, curr_fruit
                curr_count, curr_fruit = 1, fruit

        return max(max_fruits, pair_count + curr_count)


print(Solution().totalFruit([1, 2, 3, 2, 2]))
