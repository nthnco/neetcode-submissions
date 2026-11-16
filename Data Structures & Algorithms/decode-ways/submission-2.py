class Solution:
    def numDecodings(self, s: str) -> int:
        #1012
        """
        1 is valid,
        so lets go into 012
        0 is not valid so it cannot be interpreted
        10 is valid so lets go into 12
        1 is valid, so lets go to 2
        2 is also valid
        but 12 is also valid as well, 
        so base cases are you want to check if s == 2, or s == 1
        so when s == 2 if 0 < int(s) <= 26 then its a valid encoding, += 1
        and s == 1 if 0 < int(s) <= 26 then its a valid encoding as well 
        But when you get a string like 1012
        then at 1 the string returns False, so you cannot add that as a    valid way
        a valid assumptions is that a digit will always be between 0 and 26
        """
        memo = {}
        def dfs(i):
            count = 0
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]
            count = dfs(i + 1)
            if i + 1 < len(s) and int(s[i: i + 2]) <= 26:
                count += dfs(i + 2)
            memo[i] = count
            return count
        return dfs(0)
        

                



        