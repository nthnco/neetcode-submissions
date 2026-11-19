class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #text 2 is r, text1 is c

        #   c r a b t
        # c[0,0,0,0,0][0]
        # a[0,0,0,0,0][0]
        # t[0,0,0,0,1][0]
        #  [0,0,0,0,0][0]
        ROWS, COLS = len(text2) + 1, len(text1) + 1
        dp = [[0 for j in range(COLS)] for i in range(ROWS)]
        for r in range(ROWS - 2, -1, -1):
            for c in range(COLS - 2, -1, -1):
                if text2[r] == text1[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]
                else:
                    dp[r][c] = max(dp[r][c + 1],dp[r + 1][c])
        return dp[0][0]



        





        