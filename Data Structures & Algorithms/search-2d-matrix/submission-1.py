class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix[0]) - 1 
        for row in matrix:
            if target == row[start]:
                return True
            elif target == row[end]:
                return True
            elif row[start] < target and target < row[end]:
                while start <= end:
                    mid = ((end - start) // 2) + start
                    if row[mid] == target:
                        return True
                    if row[mid] < target:
                        start = mid + 1
                    else:
                        end = mid - 1
                return False
        return False

