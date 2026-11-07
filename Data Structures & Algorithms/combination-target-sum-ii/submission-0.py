class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        candidates.sort()
        def dfs(idx, cur):
            if cur == target:
                res.append(path[:])
                return
            if cur > target or idx == len(candidates):
                return
            path.append(candidates[idx])
            dfs(idx + 1, cur + candidates[idx])
            path.pop()

            while (idx + 1 < len(candidates) and 
            candidates[idx + 1] == candidates[idx]):
                idx += 1
            dfs(idx + 1, cur)
        dfs(0,0)
        return res
        
                
            


        
            

        