class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = 0
        nums = [-n for n in nums]
        heapq.heapify(nums)
        while count < k:
            ans = -1 *heapq.heappop(nums)
            count += 1
        return ans
        