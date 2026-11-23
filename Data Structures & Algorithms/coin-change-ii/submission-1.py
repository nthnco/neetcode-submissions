class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1) 
        dp[0] = 1
        for coin in coins:
            for amt in range(coin, amount + 1):
                dp[amt] += dp[amt - coin]
        return dp[amount]


        """
        0: 0
        1: 1
        2: 2
        3: 3
        4: 4
        I guess the two cases at each step they are asking is, at the current step, 
        at 1 you can ask is is there a val in coins to get to 1, and if there is then you add a step, if not then you can just extend the amt to the past one where theres a value in there, because at 1 you only have one step, at 2, you can ask you can ask if theres a coin in coin that will be able to satisfy this, and at that moment you add one, and then also ask is there a val in dp that will add up to amt - cur_amt
        """
        



        