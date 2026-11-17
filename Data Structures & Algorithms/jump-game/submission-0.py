class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for n in range(len(nums) - 2, -1,-1):
            if n + nums[n] >= goal:
                goal = n
        
        return False if goal else True


        