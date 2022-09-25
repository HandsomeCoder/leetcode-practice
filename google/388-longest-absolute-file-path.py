class Solution:
    def lengthLongestPath(self, input: str) -> int:
        parts = input.split("\n")

        stack = [-1]
        ln = 1
        max_len = 0

        for part in parts:
            sub_parts = part.split('\t')
            level = len(sub_parts)

            length = stack[level-1] + len(sub_parts[-1]) + 1

            if level == ln:
                stack.append(length)
                ln += 1
            else:
                stack[level] = length

            if "." in sub_parts[-1]:
                max_len = max(max_len, stack[level])

        return max_len