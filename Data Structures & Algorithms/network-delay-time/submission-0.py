class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1,n+1)}
        visited = set()
        ans = 0
        
        for src, dst, weight in times:
            adj[src].append([dst,weight])
        minHeap = [[0,k]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            ans = max(ans, w1)
            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap,[w1 + w2,n2])
            



        return ans if len(visited) == n else -1