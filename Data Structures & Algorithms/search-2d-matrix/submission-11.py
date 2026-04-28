class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        lr, rr = 0, len(matrix) - 1

        while lr < rr:
            middle = (lr + rr) // 2

            if target in matrix[middle]:
                return True
            elif target < matrix[middle][0]:
                rr = middle - 1
            else:
                lr = middle + 1
        
        if target in matrix[lr]:
            return True
        else:
            return False
                
        