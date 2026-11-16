class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        plan is to have the coins sorted, and fill up the coins with the largest amount you can, """
        coins.sort()
        INF = amount + 1
        dp = [INF] * INF
        dp[0] = 0
        for amt in range(1, amount + 1):
            for c in coins:
                if c <= amt:
                    dp[amt] = min(dp[amt], dp[amt - c] + 1)
        return dp[amount] if dp[amount] != INF else -1            



        
        