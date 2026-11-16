class Solution:
        

    def longestPalindrome(self, s: str) -> str:
        def palindromeLength(l, r):
            res = ""
            res_len = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_len = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
            return res_len, res

        res = ""
        res_len = 0
        for i in range(len(s)):
            odd_len, odd_res = palindromeLength(i, i)
            even_len, even_res =palindromeLength(i, i+1)
            if odd_len > even_len and odd_len > res_len:
                res_len = odd_len
                res = odd_res
            elif even_len > odd_len and even_len > res_len:
                res_len = even_len
                res = even_res 
        return res     







        