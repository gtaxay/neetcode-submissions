class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute force

        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        
        return False
        