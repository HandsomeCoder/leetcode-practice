from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        groups, sln = [], len(s)
        prev, count = s[0], 1

        for idx in range(1, sln):
            curr = s[idx]
            if prev == curr:
                count += 1
                continue

            groups.append((prev, count))
            prev, count = curr, 1
        groups.append((prev, count))

        result = 0
        for word in words:
            midx, wln, = 0, len(word)
            left = right = match = 0
            while True:
                if midx >= len(groups):
                    match = 0
                    break

                if right < wln and word[right] == groups[midx][0]:
                    right += 1
                    continue
                elif left == right:
                    break
                else:
                    curr_count = (right - left)
                    remain = groups[midx][1] - curr_count
                    if remain == 0 or (remain > 0 and (curr_count + remain) >= 3):
                        match += 1
                    else:
                        match = 0
                        break
                    left = right
                    midx += 1
                if right > wln:
                    break

            if match == len(groups):
                result += 1

        return result


print(Solution().expressiveWords(s="heeellooo", words=["hello", "hi", "helo"]))
print(Solution().expressiveWords(s="zzzzzyyyyy", words=["zzyy", "zy", "zyy"]))
