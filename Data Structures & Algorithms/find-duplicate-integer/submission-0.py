class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i in count:
                return i
            count[i] = 1
        


        