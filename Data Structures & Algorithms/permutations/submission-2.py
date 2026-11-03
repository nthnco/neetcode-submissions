class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        seen = set()
        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for n in nums:
                if n not in seen:
                    path.append(n)
                    seen.add(n)
                    backtrack()
                    path.pop()
                    seen.remove(n)
        backtrack()
        return res

        