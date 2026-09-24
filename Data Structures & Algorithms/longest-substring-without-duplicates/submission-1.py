class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        longest = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] in map:
                if map[s[r]] >= l:
                    l = map[s[r]] + 1
            map[s[r]] = r
            longest = max(longest, r - l + 1)
            r += 1


        return longest
                
            

