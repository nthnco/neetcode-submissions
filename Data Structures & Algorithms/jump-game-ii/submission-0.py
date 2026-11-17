class Solution:
    def jump(self, nums: List[int]) -> int:
        #[2,3,3,1,1,1]
        #cur_reach = i + nums[i]
        #steps = nums[i] = 2
        #max_reach = i
        #cur_steps = 3
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
        