class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)
        q = deque()
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time


        

            




        
        
        
        