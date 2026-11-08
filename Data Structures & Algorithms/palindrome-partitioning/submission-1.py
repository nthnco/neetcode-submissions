class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []
        def dfs(start):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start, len(s)):
                piece = s[start:end + 1]
                if piece == piece[::-1]:
                    path.append(piece)
                    dfs(end + 1)
                    path.pop()
        dfs(0)
        return res
                
            
            