class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for idx, val in enumerate(nums):
            if val > 0:
                break
            if idx > 0 and val == nums[idx - 1]:
                continue
            target = val
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                sum_val = nums[l] + nums[r] + target
                if sum_val == 0:
                    res.append([val,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif sum_val < 0:
                    l += 1
                else:
                    r -= 1
            
        return res
        