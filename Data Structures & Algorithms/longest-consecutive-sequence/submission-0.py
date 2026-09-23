class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for i in nums:
            length = 1
            if i - 1 in set_nums:
                continue
            else:
                sequence = i
                while sequence in set_nums:
                    if sequence + 1 in set_nums:
                        length += 1
                    sequence += 1
            longest = max(length,longest)
        return longest
