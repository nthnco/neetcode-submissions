class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        if len(s) != len(t):
            return False
        for i in s:
            map[i] = map.get(i,0) + 1
        for i in t:
            if map.get(i,0) <= 0:
                return False
            map[i] -= 1

        return True

