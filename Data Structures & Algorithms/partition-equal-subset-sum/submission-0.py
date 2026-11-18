class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0]= True
        for n in nums:
            for x in range(target, n - 1, -1):
                dp[x] = dp[x] or dp[x - n]
        return dp[target]



            

        