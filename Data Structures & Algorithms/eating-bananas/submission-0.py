class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            hours_to_eat = 0
            for i in piles:
                hours_to_eat += math.ceil(i/mid)
            if hours_to_eat <= h:
                r = mid
            else:
                l = mid + 1
        return l
