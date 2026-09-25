class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0,0
        maximum_seen = 0
        seen = {}
        while r < len(s):
            seen[s[r]] = seen.get(s[r],0) + 1
            if (r-l + 1) - max(seen.values()) > k:
                #decrease map[s[l]] by one
                seen[s[l]] -= 1
                #move l forward one step
                l += 1
            #if it is still less than k
            maximum_seen = max(maximum_seen, r-l + 1)
            r += 1
                #maximum_seen = the greater value of maximum_seen and r-l+1
        return maximum_seen
                

