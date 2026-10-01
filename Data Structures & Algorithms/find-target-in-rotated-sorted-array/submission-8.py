class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            #know we are in left side of array
            elif nums[l] <= nums[mid]:
                if nums[mid] < target or nums[l] > target:
                    l = mid + 1
                else:
                    r = mid - 1
            #know we are in right side of array
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
                
        