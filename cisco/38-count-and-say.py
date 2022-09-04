class Solution:
    def countAndSay(self, n: int) -> str:
        cache = {}
        cache[1] = ["1"]

        def say(x):
            if x not in cache:
                result = say(x-1)
                output, count, rln = [], 1, len(result)
                curr = result[0]

                for idx in range(1, rln):
                    if curr == result[idx]:
                        count += 1
                        continue
                    output.append(str(count))
                    output.append(curr)
                    count, curr = 1, result[idx]

                output.append(str(count))
                output.append(curr)
                cache[x] = output

            return cache[x]

        return "".join(say(n))

print(Solution().countAndSay(5))
