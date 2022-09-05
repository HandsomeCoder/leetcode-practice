from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def compare(log):
            _id, body = log.split(maxsplit=1)
            return (1, ) if body[0].isdigit() else (0, body, _id)

        logs.sort(key=compare)
        return logs
