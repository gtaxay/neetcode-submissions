class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # 2x2 grid
        # first val least in row
        # last value most

        # boolean exist or not

        # find row then col

        left, right = 0, len(matrix) - 1

        while left <= right:

            mid = (left + right) // 2

            # too high
            if target in matrix[mid]:
                return True
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        
        return False

        