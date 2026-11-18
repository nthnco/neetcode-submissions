class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #[2,4,-3,5, -6]
        res = max(nums)
        cur_max, cur_min = 1, 1
        for n in nums:
            if n == 0:
                cur_max, cur_min = 1, 1
            tmp = cur_max * n
            cur_max = max(tmp, cur_min * n, n)
            cur_min = min(tmp, cur_min * n, n)
            res = max(res,cur_max)
        return res