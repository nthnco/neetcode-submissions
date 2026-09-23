class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first_idx = 0
        second_idx = len(numbers) - 1
        while numbers[first_idx] + numbers[second_idx] != target:
            if numbers[first_idx] + numbers[second_idx] > target:
                second_idx -= 1
            elif numbers[first_idx] + numbers[second_idx] < target:
                first_idx += 1
        return [first_idx + 1, second_idx + 1]