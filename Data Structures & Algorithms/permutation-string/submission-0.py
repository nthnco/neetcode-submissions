class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #make a slding window of the length of s1
        # compare
        l,r = 0,len(s1) - 1 
        dict_original = {}
        for i in s1:
            dict_original[i] = dict_original.get(i,0) + 1
        while r < len(s2):
            s2_dict = {}
            l2 = l
            while l2 <= r:
                s2_dict[s2[l2]] = s2_dict.get(s2[l2],0) + 1
                l2 += 1
            if s2_dict == dict_original:
                return True
            l += 1
            r += 1
        return False

        