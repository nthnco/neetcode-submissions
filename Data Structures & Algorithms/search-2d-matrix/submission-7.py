class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_row = 0
        end_row = len(matrix) - 1 
        start = 0
        end = len(matrix[0]) - 1 
        row = None
        while start_row <= end_row:
            mid_row = ((end_row - start_row) // 2) + start_row
            if matrix[mid_row][start] > target:
                end_row = mid_row - 1
            elif matrix[mid_row][end] < target:
                start_row = mid_row + 1
            else:
                row = matrix[mid_row]
                break
        if row is None:
            return False

        while start <= end:
            mid = ((end - start) // 2) + start
            if row[mid] == target:
                return True
            if row[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

