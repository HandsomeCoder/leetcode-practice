from collections import defaultdict
from posixpath import split
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def parse(log):
            ln = len(log)
            id, first_value = [], []
            split_idx = -1
            for idx in range(ln):
                lch = log[idx]
                if lch == " ":
                    split_idx = idx
                    break
                id.append(lch)

            for idx in range(split_idx + 1,ln):
                lch  = log[idx]
                if lch == " ":
                    break
                first_value.append(lch)


            return ("".join(id), "".join(first_value), log[split_idx+1:])

        group = defaultdict(list)

        for log in logs:
            id, first_value, body = parse(log)
            if first_value.isdigit():
                group["digit"].append(log)
            else:
                group["letter"].append(body, id)

        group["letter"].sort()

        return [id + " " + body for body, id in group["letter"]] + group["digit"]
