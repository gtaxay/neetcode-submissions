class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top, bottom = 0, len(matrix) - 1

        while top <= bottom:

            mid = (top + bottom) // 2

            if target in matrix[mid]:
                return True
            elif target > matrix[mid][0]:
                top = mid + 1
            else:
                bottom = mid - 1
        
        return False
            
        