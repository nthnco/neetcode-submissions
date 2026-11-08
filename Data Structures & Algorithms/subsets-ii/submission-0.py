class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(idx, cur):
            if idx == len(nums):
                res.append(cur[:])
                return
            cur.append(nums[idx])
            backtrack(idx + 1, cur)
            cur.pop()

            while (idx + 1 < len(nums) and 
            nums[idx + 1] == nums[idx]):
                idx += 1
            backtrack(idx + 1, cur)
        backtrack(0,[])
        return res


        