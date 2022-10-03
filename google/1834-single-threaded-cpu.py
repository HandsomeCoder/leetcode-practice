from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        tln = len(tasks)
        tasks = [(tasks[idx][0], tasks[idx][1], idx) for idx in range(tln)]
        tasks.sort()

        heap_queue = []
        heapify(heap_queue)
        
        idx , time, result = 0, 0, []
        while idx < tln:
            heappush(heap_queue, (tasks[idx][1], tasks[idx][2]))
            time += tasks[idx][0]
            idx += 1
            while heap_queue:
                et, pid = heappop(heap_queue)
                result.append(pid)
                time += et
                while idx < tln and tasks[idx][0] <= time:
                    heappush(heap_queue, (tasks[idx][1], tasks[idx][2]))
                    idx += 1

        return result


print(Solution().getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]))
