# idea: for each task, add the index which it was performed
# pop the earliest one each time to minimize interval

import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = dict()
        for t in tasks:
            count[t] = count.get(t, 0)+1

        heap = [ -v for v in count.items() ]
        heapq.heapify(heap)

        # pairs of (count, idle time)
        # where count is negative for the max heap
        # and idle time is when the current task becomes available again
        timerqueue = deque()
        time = 0
        
        while heap or timerqueue:
            timer +=1
            if heap:
                count = 1 + heapq.heappop(heap)
                if count: 
                    timerqueue.append((count, time))
            if timerqueue and timerqueue[0][1] == time:
                heapq.heappush(heap,timerqueue.popleft()[0])

        return time
    


sol = Solution()

tasks = ["A","A","A","B","B","B"]
n = 2
print(sol.leastInterval(tasks, n))

# tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
# n = 1
# print(sol.leastInterval(tasks, n))