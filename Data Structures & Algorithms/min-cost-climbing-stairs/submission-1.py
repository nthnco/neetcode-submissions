class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # either +1 or +2
        #[1,2,3]top]
        #[ 1,    2,1 or 2]2 or 1 + 3
        #base cases are way[0] = 1 way[1] = 2
        cost.append(0)

        for i in range(len(cost) - 3, -1,-1):
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])
        return min(cost[0], cost[1])

