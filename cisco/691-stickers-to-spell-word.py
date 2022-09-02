from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        cache = {}

        def build_key(src):
            return tuple(sorted([(k, v) for k, v in src.items()]))

        def is_sub_dict(map1, map2):
            for key, value in map1.items():
                if key not in map2 or value <= map2[key]:
                    return False
            return True

        def find_min_combination(target_key, target_letter, stickers):
            if target_key in cache:
                return cache[target_key]

            if len(target_letter) == 0:
                return 0

            min_combination_needed = inf
            for sticker in stickers:
                removed_keys = []

                for letter, count in sticker:
                    if letter in target_letter:
                        remove_count = min(count, target_letter[letter])
                        target_letter[letter] -= remove_count
                        if target_letter[letter] == 0:
                            target_letter.pop(letter, None)
                        removed_keys.append((letter, remove_count))

                if len(removed_keys) > 0:
                    sub_target = build_key(target_letter)
                    combination = find_min_combination(sub_target, target_letter, stickers)
                    if combination != inf:
                        min_combination_needed = min(min_combination_needed, 1 + combination)
                        cache[sub_target] = combination

                for letter, count in removed_keys:
                    target_letter[letter] += count

            return min_combination_needed

        target_letter = defaultdict(lambda: 0)
        letter_needed = set()
        for tch in target:
            target_letter[tch] += 1
            letter_needed.add(tch)

        available_sticker = []
        for sticker in stickers:
            counter = defaultdict(lambda: 0)
            for sch in sticker:
                if sch in target_letter:
                    letter_needed.discard(sch)
                    counter[sch] += 1

            available_sticker.append([(k, v)for k, v in counter.items()])
            if is_sub_dict(target_letter, counter):
                return 1

        if len(letter_needed) != 0:
            return -1

        return find_min_combination(build_key(target_letter), target_letter, available_sticker)


print(Solution().minStickers(
    ["travel", "quotient", "nose", "wrote", "any"], "lastwest"))
