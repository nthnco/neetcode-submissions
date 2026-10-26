class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        prev = nums[0]
        for n in nums[1:]:
            if prev == n:
                return prev
            prev = n
    


        


        