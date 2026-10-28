class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.max_val = k
        self.nums_heap = nums
        while len(self.nums_heap) > self.max_val:
            heapq.heappop(self.nums_heap)



        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums_heap, val)
        if len(self.nums_heap) > self.max_val:
            heapq.heappop(self.nums_heap)
        return self.nums_heap[0]
            

        
