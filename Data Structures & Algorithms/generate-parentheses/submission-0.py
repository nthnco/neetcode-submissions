class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def backtrack(o,c):
            if o == c == n:
                res.append("".join(path))
            if o < n:
                path.append("(")
                backtrack(o + 1, c)
                path.pop()
            if c < o:
                path.append(")")
                backtrack(o, c + 1)
                path.pop()     
        backtrack(0,0)
        return res       


