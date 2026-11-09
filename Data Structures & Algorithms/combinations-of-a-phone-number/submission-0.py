class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        digits_map = {"2":"abc", "3":"def", "4":"ghi",
        "5":"jkl", "6":"mno", "7":"pqrs",
        "8":"tuv", "9":"wxyz",
        }
        res = []
        def dfs(idx, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            for i in digits_map[digits[idx]]:
                dfs(idx + 1, cur + i)
            return
        dfs(0, "")

        return res
        