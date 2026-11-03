class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]
        path = []

        def backtrack(idx, cur):
            if cur == target:
                res.append(path[:])
                return
            if cur > target or idx == len(nums):
                return
            path.append(nums[idx])
            backtrack(idx, cur + nums[idx])
            path.pop()
            backtrack(idx + 1, cur)
        backtrack(0,0)
        return res
        



        